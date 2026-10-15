celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

if celsius < 15:
    label = "Cold"
elif celsius <= 25:
    label = "Pleasant"
else:
    label = "Hot"
    
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F is {label}")