# sorted by left to right
# add end point of each line

import sys

def get_sorted_idx(values):
	tmp_lst = sorted((e,i) for i,e in enumerate(values))
	sorted_idx = [i[1] for i in tmp_lst]
	return sorted_idx


def collecting_signatures(all_lines, coords=[]):
	first_line = all_lines[0]
	end_point = first_line[1] - 1
	removed_lines = []
	for k in range(1, len(all_lines)):
		if all_lines[k][0] <= end_point <= all_lines[k][1] - 1:
			removed_lines.append(k)

	coords.append(str(end_point))
	all_lines = [
		all_lines[i]
		for i in range(1, len(all_lines))
		if i not in removed_lines
	]
	if len(all_lines) == 0:
		return coords

	return collecting_signatures(all_lines, coords)


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	n_segs = input_n[0][0]

	all_lines = [[x[0], x[1] + 1] for x in input_n[1:]]
	all_lines = sorted(all_lines, key=lambda x: x[1])
	coords = collecting_signatures(all_lines)

	print (len(coords))
	print (' '.join(coords))