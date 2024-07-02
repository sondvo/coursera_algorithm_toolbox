def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
	if n == 0:
		return 0

	mod = 10
	start = 0
	end = 1
	sum = 1
	find_loop = False
	for i in range(2, n + 1):
		start, end = end, (start + end) % mod
		sum += end ** 2 % mod
		if start == 0 and end == 1:
			find_loop = True
			sum -= 1
			break

	sum = sum % mod

	if find_loop is True:
		new_n = n % (i - 1)
		sum = (sum * (n // (i - 1))) % mod
		if new_n == 0:
			return sum % mod

		sum += 1
		for i in range(2, new_n + 1):
			start, end = end, start % mod + end % mod
			sum += end ** 2 % mod

	return sum % mod


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))