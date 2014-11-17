
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('-?\d*\.?\d+', numbers)

#numbers = list(map(int, input))
numbers = [float(each) for each in numbers]

mean = sum(numbers)/len(numbers)

'''
import statistics
mean = statistics.mean(numbers)
'''

print("%.2f" %mean) #precission 2