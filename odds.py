import datetime
import time
import random

# odds = [67, 43, 47, 30, 95, 71, 76, 10, 94, 12, 28, 45, 91, 7, 44, 29, 43, 14, 64, 41]
odds = []
for num in range(20):
    num = random.randint(0,100)
    odds.append(num)
print(odds)