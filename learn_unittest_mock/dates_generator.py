import calendar
from datetime import datetime, date

from dateutil.relativedelta import relativedelta


class StartEndDates:
    def __init__(self, last_week_start, last_week_end, last_month_start,
                 last_month_end):
        self.last_week_start = last_week_start
        self.last_week_end = last_week_end
        self.last_month_start = last_month_start
        self.last_month_end = last_month_end


def start_end_dates() -> StartEndDates:
    now = datetime.now()
    now_wkday = now.weekday()
    last_week_start = (now + relativedelta(days=-now_wkday - 7)).date()
    last_week_end = (now + relativedelta(days=-now_wkday - 1)).date()

    m_1 = (now + relativedelta(months=-1)).date()
    last_month_start = date(m_1.year, m_1.month, 1)
    last_month_end = date(m_1.year, m_1.month,
                          calendar.monthrange(m_1.year, m_1.month)[1])

    return StartEndDates(last_week_start, last_week_end,
                         last_month_start, last_month_end)
