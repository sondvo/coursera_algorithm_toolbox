import sys


def edit_distance(str1, str2):
	alignment_arr = [
		[0] * (len(str2) + 1)
		for i in range(len(str1) + 1)
	]

	alignment_arr[0] = [i for i in range(0, len(str2) + 1)]
	for j in range(len(str1) + 1):
		alignment_arr[j][0] += j

	# A(i, j)
	for i in range(1, len(str1) + 1):
		for j in range(1, len(str2) + 1):
			char1 = str1[i-1]
			char2 = str2[j-1]
			if char1 == char2:
				alignment_arr[i][j] = min(
					alignment_arr[i-1][j-1],
					alignment_arr[i][j-1] + 1,
					alignment_arr[i-1][j] + 1
				)
			else:
				alignment_arr[i][j] = min(
					alignment_arr[i-1][j-1] + 1,
					alignment_arr[i][j-1] + 1,
					alignment_arr[i-1][j] + 1
				)
	return alignment_arr


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	str1 = str(input_n[0].split()[0])
	str2 = str(input_n[1].split()[0])

	alignment_arr = edit_distance(str1, str2)
	print (alignment_arr[-1][-1])