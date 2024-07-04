import sys

def car_fuel(
		max_km_per_fuel,
		fuel_dis_from_start,
		res = 0
	):
	for i in range(len(fuel_dis_from_start) - 1):
		if fuel_dis_from_start[i+1] - fuel_dis_from_start[i] > max_km_per_fuel:
			return -1

	if fuel_dis_from_start[-1] <= max_km_per_fuel:
		return res

	for i in range(len(fuel_dis_from_start) - 1):
		if fuel_dis_from_start[i+1] - fuel_dis_from_start[0] > max_km_per_fuel:
			res += 1
			break

	new_fuel_dis_from_start = [x - fuel_dis_from_start[i] for x in fuel_dis_from_start[i :]]

	return car_fuel(max_km_per_fuel, new_fuel_dis_from_start, res)


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	total_distance = input_n[0][0]
	max_km_per_fuel = input_n[1][0]
	n_station = input_n[2][0]
	fuel_dis_from_start = input_n[3]
	fuel_dis_from_start = [0] + fuel_dis_from_start + [total_distance]

	print(car_fuel(
		max_km_per_fuel,
		fuel_dis_from_start
	))