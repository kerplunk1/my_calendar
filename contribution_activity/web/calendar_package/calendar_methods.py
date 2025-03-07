from calendar import Calendar
from datetime import date

cal = Calendar()

months_names = {1: "Январь",
                2: "Февраль",
                3: "Март",
                4: "Апрель",
                5: "Май",
                6: "Июнь",
                7: "Июль",
                8: "Август",
                9: "Сентябрь",
                10: "Октябрь",
                11: "Ноябрь",
                12: "Декабрь"}

def generate_calendar(year):
    all_months = []
    for i in range(1, 13):
        month = list(cal.itermonthdates(year, i))
        processed_month = []
        for day in month:
            if day.month != i:
                processed_month.append(None)
            else:
                processed_month.append(day)
        while len(processed_month) < 42:
            processed_month.append(None)
        all_months.append({'name': months_names[i], 'dates': processed_month})
    return all_months


def get_current_year():
    current_date = date.today()
    return current_date.year

