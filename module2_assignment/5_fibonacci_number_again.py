# Main idea: catch the loop where fibonacci last digit number restart as beginning

def _catch_the_end_of_the_loop(n, mod):
	if n == 0:
		return 0

	start = 0
	end = 1
	find_loop = False
	for i in range(2, n + 1):
		start, end = end, (start + end) % mod
		if start == 0 and end == 1:
			find_loop = True
			break

	return start, end, i, find_loop


def fibonacci_again(n, mod):
	start, end, i, find_loop = _catch_the_end_of_the_loop(n, mod)
	if find_loop is True:
		new_n = n % (i - 1)
		if new_n == 0:
			return 0
		for i in range(2, new_n + 1):
			start, end = end, start % mod + end % mod

	return end % mod


if __name__ == '__main__':
    n, mod = map(int, input().split())
    print(fibonacci_again(n, mod))