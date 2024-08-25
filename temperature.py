# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32


# Main function to run the temperature converter
def temperature_converter():
    while True:
        print("\nTemperature Converter:")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '2':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            print("Exiting the temperature converter.")
            break

        else:
            print("Invalid option. Please try again.")


# Step 4: Test the program with different input values
if __name__ == "__main__":
    temperature_converter()
