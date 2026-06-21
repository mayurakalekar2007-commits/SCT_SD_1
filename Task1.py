def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature():
    print("\n===== Temperature Converter =====")
    print("Scales: 1. Celsius  2. Fahrenheit  3. Kelvin")
    print("-" * 33)

    scales = {"1": "Celsius", "2": "Fahrenheit", "3": "Kelvin"}

    # Choose input scale
    while True:
        from_choice = input("Convert FROM (1/2/3): ").strip()
        if from_choice in scales:
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    # Choose output scale
    while True:
        to_choice = input("Convert TO   (1/2/3): ").strip()
        if to_choice in scales:
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    # Enter value
    while True:
        try:
            value = float(input(f"Enter temperature in {scales[from_choice]}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Validate minimum temperatures
    min_celsius = -273.15
    if from_choice == "1" and value < min_celsius:
        print(f"Error: Temperature below absolute zero ({min_celsius}°C).")
        return
    if from_choice == "2" and value < celsius_to_fahrenheit(min_celsius):
        print(f"Error: Temperature below absolute zero ({celsius_to_fahrenheit(min_celsius):.2f}°F).")
        return
    if from_choice == "3" and value < 0:
        print("Error: Kelvin cannot be negative (absolute zero = 0 K).")
        return

    # Perform conversion
    conversions = {
        ("1", "2"): celsius_to_fahrenheit,
        ("1", "3"): celsius_to_kelvin,
        ("2", "1"): fahrenheit_to_celsius,
        ("2", "3"): fahrenheit_to_kelvin,
        ("3", "1"): kelvin_to_celsius,
        ("3", "2"): kelvin_to_fahrenheit,
    }

    units = {"1": "°C", "2": "°F", "3": "K"}

    if from_choice == to_choice:
        result = value
    else:
        result = conversions[(from_choice, to_choice)](value)

    print(f"\nResult: {value} {units[from_choice]} = {result:.4f} {units[to_choice]}")

def main():
    while True:
        convert_temperature()
        again = input("\nConvert another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()