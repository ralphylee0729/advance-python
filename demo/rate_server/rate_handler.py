import threading
import socket
from datetime import date
from rates_api.rates_data import load_rates
import math

rate_history = load_rates("rates_api/rates.csv")

class rate_handler(threading.Thread):
    """some thread"""

    def __init__(self, conn: socket):
        threading.Thread.__init__(self)
        self.conn = conn

    # the run method is what runs when you call "start"
    def run(self) -> None:
        #b is shortcut of encode.utf8
        self.conn.sendall(b"connected to the rate server")

        while True:
            message =self.conn.recv(2048).decode("UTF-8")
            if not message:
                break
            #print(f"recv: {message}")
            cmd = message.split(' ')

            #for c in cmd :
            #    print(c)
            
            try:
                if (len(cmd) < 3) :
                    raise Exception("Invalid request")

                if (cmd[0].lower() != "get"):
                    raise Exception("Invalid request")
                
                for rate in rate_history:
                    #print(rate)
                    if rate["Date"] == cmd[1]:
                        # get url option base, if not found then default to EUR
                        base_country = "USD"
                        #print(base_country)

                        country_symbols = [cmd[2]]

                        #print(rate.items())

                        #create country_rates dictionary by taking each key-value pair of rate dictionary( assining key to country_code and value ot country_rate ) set the
                        # new key-value pair with (country_code, country_rate / rate[base_country]
                        country_rates = {
                            country_code: country_rate / rate[base_country]
                            for (country_code, country_rate) in rate.items()
                            if country_code != "Date"
                            and country_code in country_symbols
                            and not math.isnan(country_rate)
                        }

                        message = f'{country_rates}'
                    
            except Exception as err:
                #message = f'{err.args}'
                message = "Invalid Request"
                self.conn.sendall(message.encode("UTF-8"))
                continue


            self.conn.sendall(message.encode("UTF-8"))