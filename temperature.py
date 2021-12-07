inp = input('Enter the temperature:')
temp = int(inp)
if temp < 65:
    print("It is chilly outside")
elif temp >= 65 and temp <= 80:
    print("It is nice outside")
else:
    print("It is a warm day")
