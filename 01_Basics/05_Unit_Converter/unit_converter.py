def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("===== Unit Converter =====")

print("\n1. Kilometers → Miles")
print("2. Miles → Kilometers")
print("3. Celsius → Fahrenheit")
print("4. Fahrenheit → Celsius")

choice = input("\nChoose an option (1-4): ")

try:
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"Result: {km_to_miles(value):.2f} miles")

    elif choice == "2":
        print(f"Result: {miles_to_km(value):.2f} km")

    elif choice == "3":
        print(f"Result: {celsius_to_fahrenheit(value):.2f} °F")

    elif choice == "4":
        print(f"Result: {fahrenheit_to_celsius(value):.2f} °C")

    else:
        print("Invalid option.")

except ValueError:
    print("Please enter a valid number.")
