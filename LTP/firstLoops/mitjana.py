
import sys, re, statistics
#statistics --> python 3.4

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

numbers = list(map(int, input))

mean = statistics.mean(numbers)

#precission 2
print("%.2f" %mean)



