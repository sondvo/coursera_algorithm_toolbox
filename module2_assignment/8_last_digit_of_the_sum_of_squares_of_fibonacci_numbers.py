def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
	if n == 0:
		return 0

	res = [0, 1]
	final_sum = 1
	for i in range(2, n + 1):
		next_num = sum(res)
		res = [res[1], next_num]
		final_sum += 2 ** next_num

	return final_sum % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))