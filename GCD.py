import sys
numbers = sys.stdin.readlines()[0].split()

def GCD(a, b):
	tmp_numbers = [int(x) for x in sorted([a, b])]
	tmp_GCD = tmp_numbers[-1] % tmp_numbers[0]
	if tmp_GCD == 0:
		return tmp_numbers[0]
	return GCD(tmp_GCD, tmp_numbers[0])

print(GCD(numbers[0], numbers[1]))