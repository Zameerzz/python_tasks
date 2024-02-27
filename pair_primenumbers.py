lower_num = int(input("enter starting number: "))
upper_num = int(input("enter ending number: "))


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def display_prime_pairs(lower_num, upper_num):
    for i in range(lower_num, upper_num):
        j = i + 2
        if check_prime(i) and check_prime(j):
            print(f"prime pair: {i} & {j}")


display_prime_pairs(lower_num, upper_num)
