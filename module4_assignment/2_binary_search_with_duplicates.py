## Unsolved

import sys


def _get_sorted_idx(values):
	tmp_lst = sorted((e,i) for i,e in enumerate(values))
	sorted_idx = [i[1] for i in tmp_lst]
	return sorted_idx


def binary_search(arr, number, offset=0):
	if number < arr[0] or arr[-1] < number:
		return -1
	if number == arr[0]:
		return offset
	if number == arr[-1]:
		return offset + len(arr) - 1

	mid_idx = int(len(arr) / 2)

	if arr[mid_idx] <= number:
		offset += mid_idx
		return binary_search(arr[mid_idx :], number, offset)
	return binary_search(arr[: mid_idx], number, offset)


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	arr = input_n[1]
	target = input_n[3]
	sorted_idx = _get_sorted_idx(target)
	new_target = sorted(target)

	res = []
	final_offset = 0
	for k in range(len(new_target)):
		i = new_target[k]
		if k !=0 and i == new_target[k - 1]:
			res.append(res[-1])
			final_offset += 1
			continue

		# print ('arr, i', arr, i)
		location = binary_search(arr, i)
		if location == -1:
			res.append(location)
			continue

		res.append(final_offset + location)
		final_offset += location + 1
		arr = arr[location + 1:]
		# print ('location', location)

	final_dct = {sorted_idx[i] : res[i] for i in range(len(sorted_idx))}
	final_res = [
		final_dct[i] for i in range(len(sorted_idx))
	]
	print (' '.join(list(map(
		str,
		final_res
	))))