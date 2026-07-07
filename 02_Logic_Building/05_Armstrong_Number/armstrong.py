def is_armstrong(number):
    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number


print("===== Armstrong Number Checker =====")

print("1. Check a single number")
print("2. Find Armstrong numbers in a range")

choice = input("Choose an option (1/2): ")

try:
    if choice == "1":
        number = int(input("Enter a number: "))

        if is_armstrong(number):
            print(f"{number} is an Armstrong Number.")
        else:
            print(f"{number} is NOT an Armstrong Number.")

    elif choice == "2":
        start = int(input("Enter start: "))
        end = int(input("Enter end: "))

        print("\nArmstrong Numbers:")

        found = False

        for number in range(start, end + 1):
            if is_armstrong(number):
                print(number)
                found = True

        if not found:
            print("No Armstrong numbers found.")

    else:
        print("Invalid option.")

except ValueError:
    print("Please enter valid integers.")
