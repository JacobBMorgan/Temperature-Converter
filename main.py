print("This program will allow you to convert a temperature from one scale to another.\n"
      "Consult the following menu to make your selection:")

while True:
    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n"
          "4. Rankine\n"
          "5. Delisle\n"
          "6. Sir Isaac Newton's Degree of Temperature\n")
    sourceScale = input("What scale is your temperature measurement in? ")
    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n"
          "4. Rankine\n"
          "5. Delisle\n"
          "6. Sir Isaac Newton's Degree of Temperature\n")
    targetScale = input("What scale would you like to convert your measurement to? ")
    temperature = float(input("Finally, what's the temperature you would like to convert? "))

    # Scales match
    if sourceScale == targetScale:
        print("These scales are the same; there's no need to convert.")
        break

    # FAHRENHEIT CONVERSIONS

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

    # Fahrenheit to Rankine
    elif sourceScale == "1" and targetScale == "4":
        newTemp = temperature + 459.67
        print(round(newTemp, 2), "°R")
        break

    # Fahrenheit to Delisle
    elif sourceScale == "1" and targetScale == "5":
        newTemp = (212 - temperature) * (5/6)
        print(round(newTemp, 2), "°De")
        break

    # Fahrenheit to Newton
    elif sourceScale == "1" and targetScale == "6":
        newTemp = (temperature - 32) * (11/60)
        print(round(newTemp, 2), "°N")
        break

    # CELSIUS CONVERSIONS

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

    # Celsius to Rankine
    elif sourceScale == "2" and targetScale == "4":
        newTemp = (temperature + 273.15) * (9/5)
        print(round(newTemp, 2), "°R")
        break

    # Celsius to Delisle
    elif sourceScale == "2" and targetScale == "5":
        newTemp = (100 - temperature) * (3/2)
        print(round(newTemp, 2), "°De")
        break

    # Celsius to Newton
    elif sourceScale == "2" and targetScale == "6":
        newTemp = temperature * (33/100)
        print(round(newTemp, 2), "°N")
        break

    # KELVIN CONVERSIONS

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

    # Kelvin to Rankine
    elif sourceScale == "3" and targetScale == "4":
        newTemp = temperature * (9/5)
        print(round(newTemp, 2), "°R")
        break

    # Kelvin to Delisle
    elif sourceScale == "3" and targetScale == "5":
        newTemp = (373.15 - temperature) * (3/2)
        print(round(newTemp, 2), "°De")
        break

    # Kelvin to Newton
    elif sourceScale == "3" and targetScale == "6":
        newTemp = (temperature - 273.15) * (33/100)
        print(round(newTemp, 2), "°N")
        break

    # RANKINE CONVERSIONS

    # Rankine to Fahrenheit
    elif sourceScale == "4" and targetScale == "1":
        newTemp = temperature - 459.67
        print(round(newTemp, 2), "°F")
        break

    # Rankine to Celsius
    elif sourceScale == "4" and targetScale == "2":
        newTemp = (temperature - 491.67) * (5/9)
        print(round(newTemp, 2), "°C")
        break

    # Rankine to Kelvin
    elif sourceScale == "4" and targetScale == "3":
        newTemp = temperature * (5/9)
        print(round(newTemp, 2), "K")
        break

    # Rankine to Delisle
    elif sourceScale == "4" and targetScale == "5":
        newTemp = (671.67 - temperature) * (5/6)
        print(round(newTemp, 2), "°De")
        break

    # Rankine to Newton
    elif sourceScale == "4" and targetScale == "6":
        newTemp = (temperature - 491.67) * (11/60)
        print(round(newTemp, 2), "°N")
        break

    # DELISLE CONVERSIONS

    # Delisle to Fahrenheit
    elif sourceScale == "5" and targetScale == "1":
        newTemp = (212 - temperature) * (6/5)
        print(round(newTemp, 2), "°F")
        break

    # Delisle to Celsius
    elif sourceScale == "5" and targetScale == "2":
        newTemp = 100 - temperature * (2/3)
        print(round(newTemp, 2), "°C")
        break

    # Delisle to Kelvin
    elif sourceScale == "5" and targetScale == "3":
        newTemp = 373.15 - temperature * (2/3)
        print(round(newTemp, 2), "K")
        break

    # Delisle to Rankine
    elif sourceScale == "5" and targetScale == "4":
        newTemp = 671.67 - temperature * (11/50)
        print(round(newTemp, 2), "°R")
        break

    # Delisle to Newton
    elif sourceScale == "5" and targetScale == "6":
        newTemp = 33 - temperature * (11/50)
        print(round(newTemp, 2), "°N")
        break

    # SIR ISAAC NEWTON'S DEGREE OF TEMPERATURE CONVERSIONS

    # Newton to Fahrenheit
    elif sourceScale == "6" and targetScale == "1":
        newTemp = temperature * (60/11) + 32
        print(round(newTemp, 2), "°F")
        break

    # Newton to Celsius
    elif sourceScale == "6" and targetScale == "2":
        newTemp = temperature * (100/33)
        print(round(newTemp, 2), "°C")
        break

    # Newton to Kelvin
    elif sourceScale == "6" and targetScale == "3":
        newTemp = temperature * (100/33) + 273.15
        print(round(newTemp, 2), "K")
        break

    # Newton to Rankine
    elif sourceScale == "6" and targetScale == "4":
        newTemp = temperature * (60/11) + 491.67
        print(round(newTemp, 2), "°R")
        break

    # Newton to Delisle
    elif sourceScale == "6" and targetScale == "5":
        newTemp = (33 - temperature) * (50/11)
        print(round(newTemp, 2), "°De")
        break

    # Error handling
    else:
        print("Invalid entry; try again.")
        continue

print("Later versions of this program will support the remaining outdated temperature scales: "
      "The Réaumur and Rømer scales. Look forward to it!")
