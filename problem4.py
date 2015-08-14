#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#SOLVED

import time

def palinfind(largestnum):
    soln = []
    for i in range(largestnum, 100, -1):
        for j in range(largestnum, 100 ,-1):
            isPalindrome = True
            prod = i*j
            lstprod = list(str(prod))
            while len(lstprod) > 1:
                if lstprod.pop(0) != lstprod.pop(len(lstprod)-1):
                    isPalindrome = False
            if isPalindrome:
                soln.append(prod)
    return max(soln)
        
t0 = time.time()
print(repr(palinfind(10000)))
totaltime = time.time() - t0

print("Time elapsed: " + repr(totaltime))
