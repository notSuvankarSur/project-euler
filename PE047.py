from sympy import factorint, isprime
import time

start = time.perf_counter()
# initialised i with the smallest possible value with 4 prime factors
i = 2 * 3 * 5 * 7
# factorint returns a dictionary, containing primes as keys and exponents as values
while 1:
    # checks if 4 consecutive numbers are composite
    if isprime(i) or isprime(i+1) or isprime(i+2) or isprime(i+3):
        i += 1
        continue
    # checking for each consecutive numbers if the number of prime factors is greater or equal to 4
    if len(factorint(i)) >= 4 and len(factorint(i + 1)) >= 4 and len(factorint(i + 2)) >= 4 and len(
            factorint(i + 3)) >= 4:
        print(i)
        break
    else:
        i += 1
end = time.perf_counter()
print(end - start)
