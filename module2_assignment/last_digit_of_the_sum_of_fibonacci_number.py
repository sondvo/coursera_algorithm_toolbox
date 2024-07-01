def last_digit_of_sum_fibonacci_number(n):
	res = [0 for i in range(n)]
	res[0] = 1
	res[1] = 1
	for i in range(2, n):
		res[i] = res[i-2] + res[i-1]
	return sum(res) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_sum_fibonacci_number(input_n))