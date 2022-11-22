# Laboratory job Basics

# Data types, input/ output, calculations, Math module.

import math

# Constants
FEET_PER_YARD = 3
FEET_PER_MILE = 5280
SEC_PER_HOUR = 3600

# Function
def calcRunTime(dist1, dist2, offset, speed, coef, angle):
      offsetOnshore = dist1 * math.tan(float(angle) * math.pi / 180)
      runOverSand = math.sqrt(offsetOnshore ** 2 + dist1 ** 2)
      swim = math.sqrt((offset - offsetOnshore) ** 2 + dist2 **2)
      print(f'If a lifeguard runs at the angle of 𝜃1 = {round(float(angle))}',
            f', he will reach a drowning in {((runOverSand + swim * coef) / speed):0.1f} seconds.')

# Data input

d1 = float(input("Enter a shortest distance between the Lifeguard and waterline in yards: ")) * FEET_PER_YARD
d2 = float(input("Enter a shortest distance between the drowning man and waterline in feet: "))
h = float(input("Enter a side offset along waterline between a lifeguard and a drowning in yards: ")) * FEET_PER_YARD
vs = float(input("Enter a lifeguard speed running in sand, mph: ")) * FEET_PER_MILE / SEC_PER_HOUR
coefSlowDownWater = int(input("Enter a coefficient of lifeguard slowing down in the water, n: "))
directionSand = input("Enter an angle of running over the sand direction, °: ")

# Invoke function
calcRunTime(d1, d2, h, vs, coefSlowDownWater, directionSand)