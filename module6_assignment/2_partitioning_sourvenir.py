import sys

def go(A, T, P=[0,0,0], i=0):
	if i == len(A):
		return P[0] == T and P[1] == T and P[2] == T
	for j in range(0, len(P)):
		P[j] += A[i]
		if P[j] <= T and go(A, T, P, i+1):
			return True
		P[j] -= A[i]
	return False


def can_partition(A):
	total = sum(A)
	if total % 3 != 0:
		return False
	return go(A, total // 3)


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	N = input_n[0][0]
	A = input_n[1]
	ans = can_partition( A )
	print( int( ans ) )