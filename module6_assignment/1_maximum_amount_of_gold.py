import sys

def max_weight(total_weight, arr):
    n = len(arr)
    T = [[0] * (total_weight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, total_weight + 1):
            T[i][w] = T[i - 1][w]
            if w >= arr[i - 1]:
                weight = T[i - 1][w - arr[i - 1]] + arr[i - 1]
                if weight > T[i][w]:
                    T[i][w] = weight
    return T[n][total_weight]


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	total_weight = input_n[0][0]
	arr = sorted(input_n[1])
	print(max_weight(total_weight, arr))