import threading
import socket
from datetime import date
from rates_api.rates_data import load_rates
from rate_server.rate_database import SessionLocal, engine, Base
from rate_server.rate_models import Rate
import math
import re
from multiprocessing.sharedctypes import Synchronized
from typing import cast

rate_history = load_rates("rates_api/rates.csv")

client_command_pattern = (
    r"^(?P<command_name>[A-Z a-z]+) "
    r"(?P<market_date>[0-9]{4}-[0-9]{2}-[0-9]{2}) "
    r"(?P<currency_symbol>[A-Z]{3})$"
)

class client_counter:
    def __init__(self):
        self.counter = 0
        self.lock = lock = threading.Lock()
    def increment(self) -> None:
        self.lock.acquire()
        self.counter = self.counter + 1
        self.lock.release()
    def decrement(self) -> None:
        self.lock.acquire()
        self.counter = self.counter - 1
        self.lock.release()
    def count(self) -> int:
        return self.counter


class rate_handler(threading.Thread):
    """some thread"""

    def __init__(self, conn: socket, counter: Synchronized) :
        threading.Thread.__init__(self)
        self.conn = conn
        self.__client_command_regex = re.compile(client_command_pattern)
        self.counter = counter
        with counter.get_lock():
            counter.value = counter.value + 1
        
        Base.metadata.create_all(bind=engine)
        self.db_session = SessionLocal()

    def fetch_rate(self, dt:str) -> dict:
        for rate in rate_history:
            #print(rate)
            if rate["Date"] == dt:
                return rate
        return []

    def query_rate(self, dt: str) -> dict:
        exchange_rate = (
            self.db_session.query(Rate).filter_by(Date=dt).first()
        )

        if exchange_rate:
            return {
            "Date": exchange_rate.Date,
            "EUR": exchange_rate.EUR,
            "USD": exchange_rate.USD,
            "JPY": exchange_rate.JPY,
            "BGN": exchange_rate.BGN,
            "CYP": exchange_rate.CYP,
            "CZK": exchange_rate.CZK,
            "DKK": exchange_rate.DKK,
            "EEK": exchange_rate.EEK,
            "GBP": exchange_rate.GBP,
            "HUF": exchange_rate.HUF,
            "LTL": exchange_rate.LTL,
            "LVL": exchange_rate.LVL,
            "MTL": exchange_rate.MTL,
            "PLN": exchange_rate.PLN,
            "ROL": exchange_rate.ROL,
            "RON": exchange_rate.RON,
            "SEK": exchange_rate.SEK,
            "SIT": exchange_rate.SIT,
            "SKK": exchange_rate.SKK,
            "CHF": exchange_rate.CHF,
            "ISK": exchange_rate.ISK,
            "NOK": exchange_rate.NOK,
            "HRK": exchange_rate.HRK,
            "RUB": exchange_rate.RUB,
            "TRL": exchange_rate.TRL,
            "TRY": exchange_rate.TRY,
            "AUD": exchange_rate.AUD,
            "BRL": exchange_rate.BRL,
            "CAD": exchange_rate.CAD,
            "CNY": exchange_rate.CNY,
            "HKD": exchange_rate.HKD,
            "IDR": exchange_rate.IDR,
            "ILS": exchange_rate.ILS,
            "INR": exchange_rate.INR,
            "KRW": exchange_rate.KRW,
            "MXN": exchange_rate.MXN,
            "MYR": exchange_rate.MYR,
            "NZD": exchange_rate.NZD,
            "PHP": exchange_rate.PHP,
            "SGD": exchange_rate.SGD,
            "THB": exchange_rate.THB,
            "ZAR": exchange_rate.ZAR }
        else:
            exchange_rate = self.fetch_rate(dt)
            if exchange_rate:
                r = Rate(
                    Date = exchange_rate["Date"],
                    EUR = exchange_rate["EUR"],
                    USD = exchange_rate["USD"],
                    JPY = exchange_rate["JPY"],
                    BGN = exchange_rate["BGN"],
                    CYP = exchange_rate["CYP"],
                    CZK = exchange_rate["CZK"],
                    DKK = exchange_rate["DKK"],
                    EEK = exchange_rate["EEK"],
                    GBP = exchange_rate["GBP"],
                    HUF = exchange_rate["HUF"],
                    LTL = exchange_rate["LTL"],
                    LVL = exchange_rate["LVL"],
                    MTL = exchange_rate["MTL"],
                    PLN = exchange_rate["PLN"],
                    ROL = exchange_rate["ROL"],
                    RON = exchange_rate["RON"],
                    SEK = exchange_rate["SEK"],
                    SIT = exchange_rate["SIT"],
                    SKK = exchange_rate["SKK"],
                    CHF = exchange_rate["CHF"],
                    ISK = exchange_rate["ISK"],
                    NOK = exchange_rate["NOK"],
                    HRK = exchange_rate["HRK"],
                    RUB = exchange_rate["RUB"],
                    TRL = exchange_rate["TRL"],
                    TRY = exchange_rate["TRY"],
                    AUD = exchange_rate["AUD"],
                    BRL = exchange_rate["BRL"],
                    CAD = exchange_rate["CAD"],
                    CNY = exchange_rate["CNY"],
                    HKD = exchange_rate["HKD"],
                    IDR = exchange_rate["IDR"],
                    ILS = exchange_rate["ILS"],
                    INR = exchange_rate["INR"],
                    KRW = exchange_rate["KRW"],
                    MXN = exchange_rate["MXN"],
                    MYR = exchange_rate["MYR"],
                    NZD = exchange_rate["NZD"],
                    PHP = exchange_rate["PHP"],
                    SGD = exchange_rate["SGD"],
                    THB = exchange_rate["THB"],
                    ZAR = exchange_rate["ZAR"])
                
                self.db_session.add(r)
                self.db_session.commit()

            return exchange_rate

    # the run method is what runs when you call "start"
    def run(self) -> None:
        #b is shortcut of encode.utf8
        self.conn.sendall(b"connected to the rate server")

        while True:
            message =self.conn.recv(2048).decode("UTF-8")
            if not message:
                print("client disconected")
                break

            command_match = self.__client_command_regex.match(message)

            if command_match:
                command_parts_dict = command_match.groupdict()
                command_name = command_parts_dict["command_name"]
                market_date = command_parts_dict["market_date"]
                currency_symbol = command_parts_dict["currency_symbol"]
                print(f'cmd: {command_name}')
                print(f'date: {market_date}')
                print(f'symbol: {currency_symbol}')

            #print(f"recv: {message}")
            cmd = message.split(' ')
            #for c in cmd :
            #    print(c)
            
            try:
                if (len(cmd) < 3) :
                    raise Exception("Invalid request")

                if (cmd[0].lower() != "get"):
                    raise Exception("Invalid request")
                
                exchange_rate = self.query_rate(cmd[1])

                print(f"{exchange_rate}")

                if not exchange_rate:
                    raise Exception("Invalid request")

                            
                # get url option base, if not found then default to EUR
                base_country = "USD"
                #print(base_country)

                country_symbols = [cmd[2]]

                #print(rate.items())

                #create country_rates dictionary by taking each key-value pair of rate dictionary( assining key to country_code and value ot country_rate ) set the
                # new key-value pair with (country_code, country_rate / rate[base_country]
                country_rates = {
                    country_code: country_rate / exchange_rate[base_country]
                    for (country_code, country_rate) in exchange_rate.items()
                    if country_code != "Date"
                    and country_code in country_symbols
                    and not math.isnan(country_rate)
                }

                if not country_rates:
                    raise Exception("Invalid request")
                
                message = f'{country_rates}'
                    
            except Exception as err:
                message = f'{str(err.args)}'
                #message = "Invalid Request"
                self.conn.sendall(message.encode("UTF-8"))
                continue


            self.conn.sendall(message.encode("UTF-8"))

        with self.counter.get_lock():
            self.counter.value = self.counter.value - 1