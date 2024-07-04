def money_change(n):
    num_10 = n // 10
    num_5 = (n % 10) // 5
    num_1 = n - num_10 * 10 - num_5 * 5
    return num_10 + num_5 + num_1


if __name__ == '__main__':
    input_n = int(input())
    print(money_change(input_n))