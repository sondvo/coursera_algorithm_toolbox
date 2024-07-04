# Idea:
# group numbers into group with same prefix (eg 5, 5*, 5**)
# add suffix same as prefix so that all num have same length (eg 555, 5*5, 5**)
# corner case: [737 73] OR [373 37] => solve by adding float digit reverse to original number
# ->>> 737 -> 737.737; 73 -> 737.37
# sort

import sys

def _get_sorted_idx(values):
	tmp_lst = sorted((e,i) for i,e in enumerate(values))
	sorted_idx = [i[1] for i in tmp_lst]
	return sorted_idx


def _presorted(arr):
	suffix = str(arr[0])[0]
	max_char = sorted([len(str(x)) for x in arr])[-1]
	new_arr = []
	for i in arr:
		num_str = str(i)
		new_arr.append(
			float(
				num_str + suffix * (max_char - len(num_str)) \
				+ '.' \
				+ num_str[::-1]
			)
		)
	sorted_idx = _get_sorted_idx(new_arr)
	return [arr[i] for i in sorted_idx[::-1]]


def max_salary(numbers):
	dct = {str(i): [] for i in range(1, 10)}
	for i in numbers:
		dct[str(i)[0]].append(i)
	res = []
	for i in range(9, 0, -1):
		if dct[str(i)] == []:
			continue
		res.extend(
			_presorted(dct[str(i)])
		)
	return res


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(str, i.split())) for i in input_n]
	numbers = input_n[1]
	res = max_salary(numbers)
	print (''.join(list(map(str, res))))