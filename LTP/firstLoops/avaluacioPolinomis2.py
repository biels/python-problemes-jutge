
import sys, re

#read variable
input = sys.stdin.readline()
input = re.findall('-?\d*\.?\d+', input)
var = float(input[0])

#read coefficients
input = sys.stdin.readline()
input= re.findall('-?\d*\.?\d+', input)
coeffs = [float(each) for each in input]

numCoeffs = len(coeffs)
result = coeffs[numCoeffs - 1]

for i in range(0, numCoeffs - 1):
	result += coeffs[i] * (var**(numCoeffs - 1 - i))

print("%.4f" %result) #precission 4
