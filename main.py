while True:
    print("This program will allow you to convert a temperature from one scale to another.\n"
          "Consult the following menu to make your selection:")

    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n"
          "4. Rankine\n"
          "5. Delisle\n"
          "6. Sir Isaac Newton's Degree of Temperature\n"
          "7. Réaumur\n"
          "8. Rømer")
    sourceScale = int(input("What scale is your temperature measurement in? "))
    if sourceScale > 8 or sourceScale < 0:
        print("Invalid selection; try again.")
        continue

    print("1. Fahrenheit\n"
          "2. Celsius\n"
          "3. Kelvin\n"
          "4. Rankine\n"
          "5. Delisle\n"
          "6. Sir Isaac Newton's Degree of Temperature\n"
          "7. Réaumur\n"
          "8. Rømer")
    targetScale = int(input("What scale would you like to convert your measurement to? "))
    if targetScale > 8 or targetScale < 0:
        print("Invalid selection; try again.")
        continue

    # Scales match
    if sourceScale == targetScale:
        print("These scales are the same; there's no need to convert. Try again.")
        continue

    temperature = float(input("Finally, what's the temperature you would like to convert? "))

    # FAHRENHEIT CONVERSIONS

    # Fahrenheit to Celsius
    if sourceScale == 1 and targetScale == 2:
        newTemp = (temperature - 32) * (5/9)
        print(round(newTemp, 2), "°C")
        break

    # Fahrenheit to Kelvin
    elif sourceScale == 1 and targetScale == 3:
        newTemp = (temperature + 459.67) * (5/9)
        print(round(newTemp, 2), "K")
        break

    # Fahrenheit to Rankine
    elif sourceScale == 1 and targetScale == 4:
        newTemp = temperature + 459.67
        print(round(newTemp, 2), "°R")
        break

    # Fahrenheit to Delisle
    elif sourceScale == 1 and targetScale == 5:
        newTemp = (212 - temperature) * (5/6)
        print(round(newTemp, 2), "°De")
        break

    # Fahrenheit to Newton
    elif sourceScale == 1 and targetScale == 6:
        newTemp = (temperature - 32) * (11/60)
        print(round(newTemp, 2), "°N")
        break

    # Fahrenheit to Réaumur
    elif sourceScale == 1 and targetScale == 7:
        newTemp = (temperature - 32) * (4/9)
        print(round(newTemp, 2), "°Ré")
        break

    # Fahrenheit to Rømer
    elif sourceScale == 1 and targetScale == 8:
        newTemp = (temperature - 32) * (7/24) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # CELSIUS CONVERSIONS

    # Celsius to Fahrenheit
    elif sourceScale == 2 and targetScale == 1:
        newTemp = temperature * (9/5) + 32
        print(round(newTemp, 2), "°F")
        break

    # Celsius to Kelvin
    elif sourceScale == 2 and targetScale == 3:
        newTemp = temperature + 273.15
        print(round(newTemp, 2), "K")
        break

    # Celsius to Rankine
    elif sourceScale == 2 and targetScale == 4:
        newTemp = (temperature + 273.15) * (9/5)
        print(round(newTemp, 2), "°R")
        break

    # Celsius to Delisle
    elif sourceScale == 2 and targetScale == 5:
        newTemp = (100 - temperature) * (3/2)
        print(round(newTemp, 2), "°De")
        break

    # Celsius to Newton
    elif sourceScale == 2 and targetScale == 6:
        newTemp = temperature * (33/100)
        print(round(newTemp, 2), "°N")
        break

    # Celsius to Réaumur
    elif sourceScale == 2 and targetScale == 7:
        newTemp = temperature * (4/5)
        print(round(newTemp, 2), "°Ré")
        break

    # Celsius to Rømer
    elif sourceScale == 2 and targetScale == 8:
        newTemp = temperature * (21/40) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # KELVIN CONVERSIONS

    # Kelvin to Fahrenheit
    elif sourceScale == 3 and targetScale == 1:
        newTemp = temperature * (9/5) - 459.67
        print(round(newTemp, 2), "°F")
        break

    # Kelvin to Celsius
    elif sourceScale == 3 and targetScale == 2:
        newTemp = temperature - 273.15
        print(round(newTemp, 2), "°C")
        break

    # Kelvin to Rankine
    elif sourceScale == 3 and targetScale == 4:
        newTemp = temperature * (9/5)
        print(round(newTemp, 2), "°R")
        break

    # Kelvin to Delisle
    elif sourceScale == 3 and targetScale == 5:
        newTemp = (373.15 - temperature) * (3/2)
        print(round(newTemp, 2), "°De")
        break

    # Kelvin to Newton
    elif sourceScale == 3 and targetScale == 6:
        newTemp = (temperature - 273.15) * (33/100)
        print(round(newTemp, 2), "°N")
        break

    # Kelvin to Réaumur
    elif sourceScale == 3 and targetScale == 7:
        newTemp = (temperature - 273.15) * (4/5)
        print(round(newTemp, 2), "°Ré")
        break

    # Kelvin to Rømer
    elif sourceScale == 3 and targetScale == 8:
        newTemp = (temperature - 273.15) * (21/40) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # RANKINE CONVERSIONS

    # Rankine to Fahrenheit
    elif sourceScale == 4 and targetScale == 1:
        newTemp = temperature - 459.67
        print(round(newTemp, 2), "°F")
        break

    # Rankine to Celsius
    elif sourceScale == 4 and targetScale == 2:
        newTemp = (temperature - 491.67) * (5/9)
        print(round(newTemp, 2), "°C")
        break

    # Rankine to Kelvin
    elif sourceScale == 4 and targetScale == 3:
        newTemp = temperature * (5/9)
        print(round(newTemp, 2), "K")
        break

    # Rankine to Delisle
    elif sourceScale == 4 and targetScale == 5:
        newTemp = (671.67 - temperature) * (5/6)
        print(round(newTemp, 2), "°De")
        break

    # Rankine to Newton
    elif sourceScale == 4 and targetScale == 6:
        newTemp = (temperature - 491.67) * (11/60)
        print(round(newTemp, 2), "°N")
        break

    # Rankine to Réaumur
    elif sourceScale == 4 and targetScale == 7:
        newTemp = (temperature - 491.67) * (4/9)
        print(round(newTemp, 2), "°Ré")
        break

    # Rankine to Rømer
    elif sourceScale == 4 and targetScale == 8:
        newTemp = (temperature - 491.67) * (7/24) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # DELISLE CONVERSIONS

    # Delisle to Fahrenheit
    elif sourceScale == 5 and targetScale == 1:
        newTemp = (212 - temperature) * (6/5)
        print(round(newTemp, 2), "°F")
        break

    # Delisle to Celsius
    elif sourceScale == 5 and targetScale == 2:
        newTemp = 100 - temperature * (2/3)
        print(round(newTemp, 2), "°C")
        break

    # Delisle to Kelvin
    elif sourceScale == 5 and targetScale == 3:
        newTemp = 373.15 - temperature * (2/3)
        print(round(newTemp, 2), "K")
        break

    # Delisle to Rankine
    elif sourceScale == 5 and targetScale == 4:
        newTemp = 671.67 - temperature * (11/50)
        print(round(newTemp, 2), "°R")
        break

    # Delisle to Newton
    elif sourceScale == 5 and targetScale == 6:
        newTemp = 33 - temperature * (11/50)
        print(round(newTemp, 2), "°N")
        break

    # Delisle to Réaumur
    elif sourceScale == 5 and targetScale == 7:
        newTemp = 80 - temperature * (8/15)
        print(round(newTemp, 2), "°Ré")
        break

    # Delisle to Rømer
    elif sourceScale == 5 and targetScale == 8:
        newTemp = 60 - temperature * (7/20)
        print(round(newTemp, 2), "°Rø")
        break

    # SIR ISAAC NEWTON'S DEGREE OF TEMPERATURE CONVERSIONS

    # Newton to Fahrenheit
    elif sourceScale == 6 and targetScale == 1:
        newTemp = temperature * (60/11) + 32
        print(round(newTemp, 2), "°F")
        break

    # Newton to Celsius
    elif sourceScale == 6 and targetScale == 2:
        newTemp = temperature * (100/33)
        print(round(newTemp, 2), "°C")
        break

    # Newton to Kelvin
    elif sourceScale == 6 and targetScale == 3:
        newTemp = temperature * (100/33) + 273.15
        print(round(newTemp, 2), "K")
        break

    # Newton to Rankine
    elif sourceScale == 6 and targetScale == 4:
        newTemp = temperature * (60/11) + 491.67
        print(round(newTemp, 2), "°R")
        break

    # Newton to Delisle
    elif sourceScale == 6 and targetScale == 5:
        newTemp = (33 - temperature) * (50/11)
        print(round(newTemp, 2), "°De")
        break

    # Newton to Réaumur
    elif sourceScale == 6 and targetScale == 7:
        newTemp = temperature * (80/33)
        print(round(newTemp, 2), "°Ré")
        break

    # Newton  to Rømer
    elif sourceScale == 6 and targetScale == 8:
        newTemp = temperature * (35/22) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # REAUMUR CONVERSIONS

    # Réaumur to Fahrenheit
    elif sourceScale == 7 and targetScale == 1:
        newTemp = temperature * (9/4) + 32
        print(round(newTemp, 2), "°F")
        break

    # Réaumur to Celsius
    elif sourceScale == 7 and targetScale == 2:
        newTemp = temperature * (5/4)
        print(round(newTemp, 2), "°C")
        break

    # Réaumur to Kelvin
    elif sourceScale == 7 and targetScale == 3:
        newTemp = temperature * (5/4) + 273.15
        print(round(newTemp, 2), "K")
        break

    # Réaumur to Rankine
    elif sourceScale == 7 and targetScale == 4:
        newTemp = temperature * (9/4) + 491.67
        print(round(newTemp, 2), "°R")
        break

    # Réaumur to Delisle
    elif sourceScale == 7 and targetScale == 5:
        newTemp = (80 - temperature) * (15/8)
        print(round(newTemp, 2), "°De")
        break

    # Réaumur to Newton
    elif sourceScale == 7 and targetScale == 6:
        newTemp = temperature * (33/80)
        print(round(newTemp, 2), "°N")
        break

    # Réaumur to Rømer
    elif sourceScale == 7 and targetScale == 8:
        newTemp = temperature * (21/32) + 7.5
        print(round(newTemp, 2), "°Rø")
        break

    # ROMER CONVERSIONS

    # Rømer to Fahrenheit
    elif sourceScale == 8 and targetScale == 1:
        newTemp = (temperature - 7.5) * (24/7) + 32
        print(round(newTemp, 2), "°F")
        break

    # Rømer to Celsius
    elif sourceScale == 8 and targetScale == 2:
        newTemp = (temperature - 7.5) * (40/21)
        print(round(newTemp, 2), "°C")
        break

    # Rømer to Kelvin
    elif sourceScale == 8 and targetScale == 3:
        newTemp = (temperature - 7.5) * (40/21) + 273.15
        print(round(newTemp, 2), "K")
        break

    # Rømer to Rankine
    elif sourceScale == 8 and targetScale == 4:
        newTemp = (temperature - 7.5) * (24/7) + 491.67
        print(round(newTemp, 2), "°R")
        break

    # Rømer to Delisle
    elif sourceScale == 8 and targetScale == 5:
        newTemp = (60 - temperature) * (20/7)
        print(round(newTemp, 2), "°De")
        break

    # Rømer to Newton
    elif sourceScale == 8 and targetScale == 6:
        newTemp = (temperature - 7.5) * (22/35)
        print(round(newTemp, 2), "°N")
        break

    # Rømer to Réaumur
    elif sourceScale == 8 and targetScale == 7:
        newTemp = (temperature - 7.5) * (32/21)
        print(round(newTemp, 2), "°Ré")
        break

    # Error handling
    else:
        print("Invalid entry; try again.")
        continue

print("Thank you for using my converter!")
