from _datetime import datetime

date = datetime.today()
date1 = datetime.now()
date2 = date.strftime("%d-%m-%Y %H")
print(date2)