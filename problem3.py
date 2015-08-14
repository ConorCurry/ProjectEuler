#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Can be optimized with dynamic programming (see problem2)

#SOLVED

import time

solution = []

def primefactors(n):
    isPrime = True
    for i in range(n//2 + 1):
        if i != 0 and i != 1 and n % i == 0:
            isPrime = False
            p1 = primefactors(i)
            if p1:
                solution.append(p1)
            p2 = primefactors(n//i)
            if p2:
                solution.append(p2)
            break
    if isPrime:
        return n
            
t0 = time.time()
isPrime = bool(primefactors(600851475143))
totaltime = time.time() - t0

print("Elapsed time: " + repr(totaltime))
print("Is input prime? " + repr(isPrime))
print("Prime factors found: " + repr(solution))
print("Greatest prime factor: " + repr(max(solution)))
