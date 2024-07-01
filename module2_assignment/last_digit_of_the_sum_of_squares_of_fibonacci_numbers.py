def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
	res = [0 for i in range(n)]
	ss_res = [0 for i in range(n)]
	res[0] = 1
	ss_res[0] = 1
	res[1] = 1
	ss_res[1] = 1
	for i in range(2, n):
		res[i] = res[i-2] + res[i-1]
		ss_res[i] = res[i] ** 2
	return sum(res)


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))