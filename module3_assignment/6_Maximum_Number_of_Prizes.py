def max_num_of_prize(n):
	for i in range(1, n + 1):
		if i * (i + 1) / 2 > n:
			break

	max_n = i - 1
	res = [0] + [i for i in range(1, max_n + 1)]

	while n - sum(res) <= res[-1]:
		res = res[:-1]

	res.append(n - sum(res))
	return res[1:]


if __name__ == '__main__':
	input_n = int(input())
	nums = max_num_of_prize(input_n)
	print (len(nums))
	print (' '.join([str(x) for x in nums]))