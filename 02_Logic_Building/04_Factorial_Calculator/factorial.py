def factorial_iterative(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


print("===== Factorial Calculator =====")

try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        print("\nIterative Result :", factorial_iterative(number))
        print("Recursive Result :", factorial_recursive(number))

except ValueError:
    print("Please enter a valid integer.")
