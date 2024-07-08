import sys

def max_weight(total_weight, arr):
    optimal_weight = [
        [0] * (total_weight + 1)
        for _ in range(len(arr) + 1)
    ]
    for i in range(1, len(arr) + 1):
        adding_weight = arr[i-1]
        for w in range(1, total_weight+1):
            optimal_weight[i][w] = optimal_weight[i-1][w]
            if adding_weight <= w:
                optimal_weight[i][w] = max(
                    optimal_weight[i-1][w-adding_weight] + adding_weight,
                    optimal_weight[i][w]
                )
        # print (optimal_weight)
    return optimal_weight


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	total_weight = input_n[0][0]
	arr = sorted(input_n[1])
	print(max_weight(total_weight, arr)[-1][-1])