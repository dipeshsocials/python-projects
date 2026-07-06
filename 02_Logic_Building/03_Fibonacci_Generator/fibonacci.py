def fibonacci_count(n):
    sequence = []

    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def fibonacci_limit(limit):
    sequence = []

    a, b = 0, 1

    while a <= limit:
        sequence.append(a)
        a, b = b, a + b

    return sequence


print("===== Fibonacci Generator =====")

print("1. Generate first N Fibonacci numbers")
print("2. Generate Fibonacci numbers up to a limit")

choice = input("Choose an option (1/2): ")

try:
    value = int(input("Enter a number: "))

    if value < 0:
        print("Please enter a non-negative integer.")

    elif choice == "1":
        print(fibonacci_count(value))

    elif choice == "2":
        print(fibonacci_limit(value))

    else:
        print("Invalid option.")

except ValueError:
    print("Please enter a valid integer.")
