# Temperature conversion program
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin 

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return celsius

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin ")
    print("4. Kelvin to Celsius")
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice==3:
        celsius = float(input("Enter temperature in Celsius: "))  
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {kelvin:.2f}K")
    elif choice==4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin}K is equal to {celsius:.2f}°C")
    else:
        print("Invalid conversion") 

