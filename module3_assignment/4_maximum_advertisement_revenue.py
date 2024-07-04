import sys


def max_adv_revenue(n_slots, prices_seq, clicks_seq):
	res = 0
	for i in range(n_slots):
		res += prices_seq[i] * clicks_seq[i]
	return res


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	n_slots = input_n[0][0]
	prices_seq = input_n[1]
	clicks_seq = input_n[2]

	print (
		max_adv_revenue(
			n_slots,
			sorted(prices_seq)[::-1],
			sorted(clicks_seq)[::-1]
		)
	)