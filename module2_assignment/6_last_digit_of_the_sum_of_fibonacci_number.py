# Main idea: catch the loop where fibonacci last digit number restart as beginning

def _catch_the_end_of_the_loop(n, mod):
	i = 0
	if n == 0:
		return 0, 0, 0, i, False

	start = 0
	end = 1
	sum = 1
	find_loop = False
	for i in range(2, n + 1):
		start, end = end, (start + end) % mod
		sum += end
		if start == 0 and end == 1:
			find_loop = True
			sum -= 1
			break

	sum = sum % mod

	return start, end, sum, i, find_loop


def last_digit_of_sum_fibonacci_number(n):
	mod = 10
	start, end, sum, i, find_loop = _catch_the_end_of_the_loop(n, mod)
	if find_loop is True:
		new_n = n % (i - 1)
		sum = (sum * (n // (i - 1))) % mod

		if new_n == 0:
			return sum % mod

		sum += 1
		for i in range(2, new_n + 1):
			start, end = end, start % mod + end % mod
			sum += end

	return sum % mod


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_sum_fibonacci_number(input_n))