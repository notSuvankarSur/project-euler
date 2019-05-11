from fractions import Fraction

frac = [1]
for i in range(1000):
    frac.append(2)

count = 0

for i in range(1, 1001):
    temp = Fraction(frac[i - 1]) + Fraction(1 / frac[i])
    for j in range(i - 1, 0, -1):
        temp = Fraction(frac[i - 1]) + Fraction(1 / temp)
    temp = Fraction(temp - 1)
    if len(str(Fraction(temp).numerator)) > len(str(Fraction(temp).denominator)):
        count += 1
    del temp

print(count)
