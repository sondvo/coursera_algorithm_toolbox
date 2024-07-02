def fibonacci_number(n):
	if n < 2:
		res = [0, 1]
	else:
		res = [0 for i in range(n+1)]
		res[1] = 1
		for i in range(2, n+1):
			res[i] = res[i-2] + res[i-1]
	return res[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))