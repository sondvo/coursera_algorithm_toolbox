# I am only familiar with python right now...
import sys

if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	arr = sorted(input_n[1])
	print (' '.join(list(map(str, arr))))