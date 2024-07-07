# Unsolved...

import sys

if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	original_arr = input_n[1]
	res = 0
	for i in range(len(original_arr)):
		tmp_arr = original_arr[i:]
		res += tmp_arr.index(i)
	print (res)