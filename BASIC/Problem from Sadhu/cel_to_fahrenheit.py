def change_to_fahrenheit(celsius) :
    fahrenheit = ((celsius * 9) / 5 ) + 32
    return fahrenheit

fahrenheit = change_to_fahrenheit(float(input("Type in a temperature in Celsius: ")))
print("That is {} degrees Fahrenheit".format(fahrenheit))
    