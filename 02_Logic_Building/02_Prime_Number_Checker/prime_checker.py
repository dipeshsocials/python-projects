import math


def is_prime(number):
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1

    for i in range(3, limit, 2):
        if number % i == 0:
            return False

    return True


print("===== Prime Number Checker =====")

try:
    number = int(input("Enter an integer: "))

    if is_prime(number):
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is NOT a Prime Number.")

except ValueError:
    print("Please enter a valid integer.")
