import datetime
import time

data = datetime.date.today()
print(data)

dataString = datetime.date.isoformat(datetime.date.today())
print(dataString)

hora = time.strftime("%H:%M")
print(hora)

hora2 = time.strftime("%A:%p")
print(hora2)