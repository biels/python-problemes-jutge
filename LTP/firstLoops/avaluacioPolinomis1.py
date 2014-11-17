
import sys, re

#read variable
var = sys.stdin.readline()
var = re.findall('-?\d*\.?\d+', var)
var = float(var[0])

#read coefficients
coeffs = sys.stdin.readline()
coeffs = re.findall('-?\d*\.?\d+', coeffs)
coeffs = [float(each) for each in coeffs]

numCoeffs = len(coeffs)
result = coeffs[0]

for i in range(1, numCoeffs):
	result += coeffs[i] * var**i

print("%.4f" %result) #precission 4'''
