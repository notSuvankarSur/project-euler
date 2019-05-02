from fractions import Fraction

cont_frac = [2]
for i in range(1, 101):
    # generating the continued fraction of e, already appending 2
    cont_frac.append(1)
    cont_frac.append(2 * i)
    cont_frac.append(1)

# this is the final fraction, the base one
# then recursively evaluated the fraction
temp = Fraction(cont_frac[98]) + Fraction(1 / cont_frac[99])
for i in range(97, -1, -1):
    temp = Fraction(cont_frac[i]) + Fraction(1 / temp)

s = 0
for i in str(Fraction(temp).numerator):
    s += int(i)

print(s)
