
import sys, re

#read variable
var = sys.stdin.readline()
var = re.findall('-?\d*\.?\d+', var)
var = float(var[0])

#read coefficients
coeffs = sys.stdin.readline()
coeffs= re.findall('-?\d*\.?\d+', coeffs)
coeffs = [float(each) for each in coeffs]

numCoeffs = len(coeffs)
result = coeffs[numCoeffs - 1]

for i in range(0, numCoeffs - 1):
	result += coeffs[i] * (var**(numCoeffs - 1 - i))

print("%.4f" %result) #precission 4
