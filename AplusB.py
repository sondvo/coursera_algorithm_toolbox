tmp_numbers = input()
numbers = tmp_numbers.split()
numbers = [float(x) for x in numbers]

print (int(sum(numbers)))
