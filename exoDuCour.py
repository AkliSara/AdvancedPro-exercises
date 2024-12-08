f = float(input("Enter the temperature in Fahrenheit: "))
c = 5 / 9 * (f - 32)
print(f"The equivalent temperature in Celsius is:{c}°C")
if c < 0:
    print("Brr! It's cold in here!")
