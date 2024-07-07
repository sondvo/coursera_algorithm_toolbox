import sys


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	arr = input_n[1]
	arr = sorted(arr)
	if len(arr) % 2 == 1:
		middle_idx = int(len(arr) / 2)
		num = arr[middle_idx]
		if arr.count(num) > len(arr) / 2:
			print (1)
		else:
			print (0)
	else:
		first_idx = int(len(arr) / 2) - 1
		second_idx = int(len(arr) / 2)
		if arr[first_idx] != arr[second_idx]:
			print (0)
		else:
			num = arr[first_idx]
			if arr.count(num) > len(arr) / 2:
				print (1)
			else:
				print (0)
