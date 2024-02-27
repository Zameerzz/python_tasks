fahrenheit = int(input("please enter temperature in fahrenheit:"))

def show_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 * (fahrenheit - 32)/9
    print(celsius)
    return celsius
show_fahrenheit_to_celsius(fahrenheit)