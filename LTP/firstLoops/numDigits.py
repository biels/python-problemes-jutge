
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

number = number[0]
numDigits = len(number) 

print("El nombre de digits de %s es %d."%(number, numDigits))