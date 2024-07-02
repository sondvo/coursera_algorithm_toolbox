def last_digit_of_sum_fibonacci_number_again(ss, ee):
	if n == 0:
		return 0

	res = [0, 1]
	final_sum = 1
	for i in range(2, n + 1):
		next_num = sum(res)
		res = [res[1], next_num]
		final_sum += next_num

	return final_sum % 10


if __name__ == '__main__':
    ss, ee = map(int, input().split())
    print(last_digit_of_sum_fibonacci_number_again(ss, ee))