# Laboratory job Basics

# Data types, input/ output, calculations, Math module.

import math

# Constants
FEETperYARD = 3
FEETperMILE = 5280
SECperHOUR = 3600

# Data input

d1 = float(input("Enter a shortest distance between the Lifeguard and waterline in yards: ")) * FEETperYARD
d2 = float(input("Enter a shortest distance between the drowning man and waterline in feet: "))
h = float(input("Enter a side offset along waterline between a lifeguard and a drowning in yards: ")) * FEETperYARD
vs = float(input("Enter a lifeguard speed running in sand, mph: ")) * FEETperMILE / SECperHOUR
coefSlowDownWater = int(input("Enter a coefficient of lifeguard slowing down in the water, n: "))
directionSand = input("Enter an angle of running over the sand direction, °: ")
theta1 = float(directionSand) * math.pi / 180   # convert to rad.

# Calculations

x = d1 * math.tan(theta1)     # offset between position of a lifeguard and point of entry into water. Feet.
L1 = math.sqrt(x ** 2 + d1 ** 2)    # distance between lifeguard position and point of entry into water. Feet.
L2 = math.sqrt((h - x) ** 2 + d2 ** 2)  # distance between point of entry into water and a drowning. Feet.
timeSalvage = (L1 + L2 * coefSlowDownWater) / vs

# Output result

print(f'If a lifeguard runs at the angle of 𝜃1 = {round(float(directionSand))}',
      f', he will reach a drowning in {timeSalvage:0.1f} seconds.')