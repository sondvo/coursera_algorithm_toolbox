import sys


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(str, i.split())) for i in input_n]
	numbers = input_n[1]
	print (''.join(sorted(numbers)[::-1]))