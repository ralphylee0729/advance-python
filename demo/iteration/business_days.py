from datetime import date
from datetime import timedelta
import holidays


def business_days(start_date, end_date) -> list[date] :
    us_pr_holidays = holidays.country_holidays('US', subdiv='PR')
    working_days = []
    for n in range(int((end_date - start_date).days)):
        d = start_date + timedelta(n)
        if (d not in us_pr_holidays and d.weekday() !=  5 and d.weekday() != 6) :
            working_days.append(d)

    return working_days


if __name__ == "__main__" :
    working_days = business_days(date(2024, 1, 1,), date(2024, 1, 10))
    print(working_days)