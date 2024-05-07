from iteration.business_days import business_days
from datetime import date
import requests

def get_exchange_rate(working_days) -> list[str]:
    rates =  []
    for day in working_days:
        url=f"http://127.0.0.1:8900/api/{day}?base=USD&symbols=EUR"
        #print(url)
        r = requests.get(url)
        #print(r.text)
        rates.append(r.text)
    return rates


if __name__ == "__main__" :
    rates = get_exchange_rate(business_days(date(2021, 1, 1,), date(2021, 1, 10)))
    print(rates)