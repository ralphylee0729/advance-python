import requests
from datetime import date
from datetime import timedelta
import holidays


def exchange_rate(start_date, end_date) -> list[str] :
    us_pr_holidays = holidays.country_holidays('US', subdiv='PR')
    rates = []
    for n in range(int((end_date - start_date).days)):
        d = start_date + timedelta(n)
        if (d not in us_pr_holidays and d.weekday() !=  5 and d.weekday() != 6) :
            url=f"http://127.0.0.1:8900/api/{d}?base=USD&symbols=EUR"
            r = requests.get(url)
            rates.append(r.text)

    return rates


if __name__ == "__main__" :
    rates = exchange_rate(date(2021, 1, 1,), date(2021, 1, 10))
    print(rates)
