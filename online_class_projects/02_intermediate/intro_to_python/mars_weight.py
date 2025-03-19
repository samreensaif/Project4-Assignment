
print("Welcome to Mars Weight Calculator")
print("="*34)



MERCURY = 0.376 
VENUS = 0.889 
MARS = 0.378 
JUPITER = 2.36 
SATURN = 1.081 
URANUS = 0.815 
NEPTUNE = 1.14 
EARTH = 1.0

ask = (input("on which planet u want to check ur weight? ")).lower()

if ask == "mercury":
  const = MERCURY
elif ask == "venus":
  const = VENUS
elif ask == "mars":
  const = MARS
elif ask == "jupiter":
  const = JUPITER
elif ask == "saturn":
  const = SATURN
elif ask == "uranus":
  const = URANUS
  
elif ask == "neptune":
  const = NEPTUNE
else:
  const = EARTH


earth_weight = float (input("enter weight on earth: "))

weight  = earth_weight * const

print (f"your weight on {ask}: {round(weight,2)} kg")
