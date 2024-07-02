def last_digit_fibonacci_number(n):
	if n == 0:
		return 0

	start = 0
	end = 1
	for i in range(2, n + 1):
		start, end = end % 10, (start + end) % 10
	return end % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_fibonacci_number(input_n))