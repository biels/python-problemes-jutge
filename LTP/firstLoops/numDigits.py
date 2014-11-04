
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

number = input[0]
numDigits = len(number) 

print("El nombre de digits de %s es %d."%(number, numDigits))