#  as we know 10 power anything will give exponent+1 digits, so we only need to check for 1 to 9
#  as for exponents it's just hit and try, program modified after execution
digit = 1
count = 1
while digit < 25:
    number = 2
    while number < 10:
        if len(str(number ** digit)) == digit:
            count += 1
            print(number, digit)
        if len(str(number ** digit)) > digit:
            digit += 1
            break
        number += 1
    digit += 1

print(count)


