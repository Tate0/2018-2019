'''
get name, distance travelled, duration of travel from user
calculate speed
print greeting by name and display speed
'''

name = input("What is your name? ")
disTrav = float(input("What distance did you travel: "))
durTrav = float(input("What is your duration of travel: "))

speed = int(disTrav/durTrav)

print("Hello", name + ",",
      "your speed was:",
      speed, "km/h")
