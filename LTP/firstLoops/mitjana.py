
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d*\.?\d+', input)

#numbers = list(map(int, input))
numbers = [float(each) for each in input]

mean = sum(numbers)/len(numbers)

'''
import statistics
mean = statistics.mean(numbers)
'''

print("%.2f" %mean) #precission 2
