print("This program will allow you to convert a temperature from one scale to another.\n"
      "Consult the following menu to make your selection:")

while True:
    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n")
    sourceScale = input("What scale is your temperature measurement in? ")
    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n")
    targetScale = input("What scale would you like to convert your measurement to? ")
    temperature = float(input("Finally, what's the temperature you would like to convert? "))

    # Scales match
    if sourceScale == targetScale:
        print("These scales are the same; there's no need to convert.")

    # Fahrenheit to Celsius
    elif sourceScale == "1" and targetScale == "2":
        newTemp = (temperature - 32) * (5/9)
        print(round(newTemp, 2), "°C")
        break

    # Fahrenheit to Kelvin
    elif sourceScale == "1" and targetScale == "3":
        newTemp = (temperature + 459.67) * (5/9)
        print(round(newTemp, 2), "K")
        break

    # Celsius to Fahrenheit
    elif sourceScale == "2" and targetScale == "1":
        newTemp = temperature * (9/5) + 32
        print(round(newTemp, 2), "°F")
        break

    # Celsius to Kelvin
    elif sourceScale == "2" and targetScale == "3":
        newTemp = temperature + 273.15
        print(round(newTemp, 2), "K")
        break

    # Kelvin to Fahrenheit
    elif sourceScale == "3" and targetScale == "1":
        newTemp = temperature * (9/5) - 459.67
        print(round(newTemp, 2), "°F")
        break

    # Kelvin to Celsius
    elif sourceScale == "3" and targetScale == "2":
        newTemp = temperature - 273.15
        print(round(newTemp, 2), "°C")
        break

    # Error handling
    else:
        print("Invalid entry; try again.")
        continue

print("Later versions of this program may support outdated temperature scales, such as: Rankine, Delisle, "
      "Sir Isaac Newton's Degree of Temperature, Réaumur, and Rømer scales. Look forward to it!")
