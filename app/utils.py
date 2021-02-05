import calendar
import datetime

def format_date(card_exp_date):

    month, year = card_exp_date.split("/")
    monthrange = calendar.monthrange(int(year), int(month))
    last_day = monthrange[1]
    full_date = f"{year}-{month}-{last_day}"
    # date_obj = datetime.datetime.strptime(full_date, "%Y-%m-%d").date()

    return full_date
