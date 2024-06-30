import sys
numbers = sys.stdin.readlines()
numbers = numbers[1]
numbers = sorted([int(x) for x in numbers.split()])
print (numbers[-2] * numbers[-1])
