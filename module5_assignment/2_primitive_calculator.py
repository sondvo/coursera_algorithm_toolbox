# +1, x2, x3

def _get_sorted_idx(values):
	tmp_lst = sorted((e,i) for i,e in enumerate(values))
	sorted_idx = [i[1] for i in tmp_lst]
	return sorted_idx


def primitive_cal(num):
	final_res = [0, 0, 1, 1]
	min_cases = [None, 1, 2 ,3]
	if num < 4:
		return final_res[num], [1, num][:num]

	for i in range(4, num + 1):
		case1 = final_res[-1] + 1
		case2 = final_res[i//2] + 1 + i%2
		case3 = final_res[i//3] + 1 + i%3

		order = _get_sorted_idx([case1, case2, case3])
		min_cases.append(order[0] + 1)

		final_res.append(
			min(case1, case2, case3)
		)

	seq = [num]
	while num > 3:
		if min_cases[num] == 1:
			num -= 1
		elif min_cases[num] == 2:
			num = num // 2
		elif min_cases[num] == 3:
			num = num // 3

		seq.append(num)

	seq = seq[::-1]
	return final_res[-1], [1] + seq


if __name__ == '__main__':
	input_n = int(input())
	a, b = primitive_cal(input_n)
	print (a)
	print (' '.join(list(map(str, b))))