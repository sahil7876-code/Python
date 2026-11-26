from datetime import date
from datetime import datetime
from datetime import timedelta
import time


a = date.today()
print(a)
print(datetime.now())
b = datetime.now()
print(b.time())
print(b.date())

x = timedelta(3, 5, 0, 0, )
y =timedelta(7.5)

print(x)
print(y)
print(x+y)
