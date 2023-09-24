def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    print("Temperature Unit Conversion")
    print("Supported units: Celsius, Fahrenheit, Kelvin")

    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    if original_unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"Converted Fahrenheit: {fahrenheit} °F")
        print(f"Converted Kelvin: {kelvin} K")
    elif original_unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"Converted Celsius: {celsius} °C")
        print(f"Converted Kelvin: {kelvin} K")
    elif original_unit == 'kelvin':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"Converted Celsius: {celsius} °C")
        print(f"Converted Fahrenheit: {fahrenheit} °F")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

if __name__ == "__main__":
    temperature_conversion()
