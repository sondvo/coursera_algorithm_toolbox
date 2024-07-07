# 1, 3, 4
def money_change(num):
	final_res = [0, 1, 2, 1, 1]
	for i in range(5, num + 1):
		final_res.append(min(
			final_res[-1] + 1,
			final_res[i - 3] + 1,
			final_res[i - 4] + 1,
		))

	return final_res[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(money_change(input_n))