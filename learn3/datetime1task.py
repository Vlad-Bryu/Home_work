from datetime import datetime, timedelta

dt_now = datetime.now().strftime('%Y %m %d')
print("Дата сегодня: ", dt_now)

dt_now = datetime.now().strptime(dt_now, '%Y %m %d')
delta_tomorrow = timedelta(days=1)
dt_tomorrow = dt_now - delta_tomorrow
print("Дата вчера: ", dt_tomorrow.strftime('%Y %m %d'))

delta_month = timedelta(days=30)
dt_month = dt_now - delta_month
print("Дата месяц назад (30 дней): ", dt_month.strftime('%Y %m %d'))

date_string = "01/01/17 12:10:03.234567"
string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print("Тип строки: ", type(string))




