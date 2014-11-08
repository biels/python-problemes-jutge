
import sys, re
#from fractions import gcd

def gcd(a, b):

    while (b != 0):
        (a, b) = (b, a%b)
    return a


input = sys.stdin.readline()
input = re.findall('-?\d+', input)

numbers = list(map(int, input))

gcd = gcd(numbers[0], numbers[1])

print('El mcd de %d i %d es %d.' %(numbers[0], numbers[1], gcd))

