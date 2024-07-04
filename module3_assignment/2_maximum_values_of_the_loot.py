import sys

def max_loot(total_weight, properties):
	final_values=0

	for pro in properties[:-1]:
		cost, weight = pro

		if weight > total_weight:
			final_values += total_weight * cost / weight
			return final_values

		final_values += cost
		total_weight -= weight

		if total_weight == 0:
			return final_values

	if total_weight > properties[-1][1]:
		return final_values + properties[-1][0]

	return final_values + total_weight * properties[-1][0] / properties[-1][1]


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	n_compounds, total_weight = input_n[0]

	properties = input_n[1:]
	values = [i[0] / i[1] for i in properties]
	tmp_lst = sorted((e,i) for i,e in enumerate(values))
	sorted_idx = [i[1] for i in tmp_lst][::-1]
	properties = [properties[i] for i in sorted_idx]

	print(max_loot(total_weight, properties))