import decimal
import math

total = 0
decimal.getcontext().prec = 103
# setting the precision to more than 100 digits, as rounding off takes place, which affects the precision
# this is important as I have encountered multiple wrong answers due to the rounding
for num in range(2, 100):
    if math.sqrt(num) == int(math.sqrt(num)):
        continue
    dec = decimal.Decimal(num).sqrt()
    print(num, dec)
    for i in range(101):
        if str(dec)[i].isdecimal():
            total += int(str(dec)[i])


print(total)
