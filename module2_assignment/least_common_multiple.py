def LOM(a, b):
	numbers = sorted([a, b])
	lower = numbers[0]
	upper = numbers[1]
	for i in range(1, lower):
		tmp_res = upper*i
		if tmp_res % lower == 0:
			return tmp_res


if __name__ == '__main__':
    input_n = input()
    input_n = [int(i) for i in input_n.split()]
    print(LOM(*input_n))