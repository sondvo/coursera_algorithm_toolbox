def GCD(a, b):
	tmp_numbers = [int(x) for x in sorted([a, b])]
	tmp_GCD = tmp_numbers[-1] % tmp_numbers[0]
	if tmp_GCD == 0:
		return tmp_numbers[0]
	return GCD(tmp_GCD, tmp_numbers[0])

if __name__ == '__main__':
    input_n = input()
    input_n = [int(i) for i in input_n.split()]
    print(GCD(*input_n))