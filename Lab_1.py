# Laboratory job #1.

# Data types, input/ output, calculations, Math module.

# Data input

import math

# Shortest distance between a lifeguard and a waterline, yards.
distLifeguardWater = input("Enter a shortest distance between the Lifeguard and waterline in yards: ")
d1 = float(distLifeguardWater) * 3  # convert to feet.
# Shortest distance between a waterline and a drowning, feet.
distWaterSurvivor = input("Enter a shortest distance between the drowning man and waterline in feet: ")
d2 = float(distWaterSurvivor)   # in feet.
# Side offset along waterline between a lifeguard and a drowning, yards.
offset = input("Enter a side offset along waterline between a lifeguard and a drowning in yards: ")
h = float(offset) * 3   # convert to feet.
# Velocity through the sand, mph.
velocitySand = input("Enter a lifeguard speed running in sand, mph: ")
vs = float(velocitySand) * 5280/3600    # convert to feet per seconds.
# Lifeguard slow down coefficient in the water, n.
coefSlowDownWater = int(input("Enter a coefficient of lifeguard slowing down in the water, n: "))
# Running over the sand direction, °.
directionSand = input("Enter an angle of running through the sand direction, °: ")
theta1 = float(directionSand) * math.pi / 180   # convert to rad.

# Calc

x = d1 * math.tan(theta1)     # offset between position of a lifeguard and point of entry into water. Feet.

L1 = math.sqrt(x ** 2 + d1 ** 2)    # distance between lifeguard position and point of entry into water. Feet.

L2 = math.sqrt((h - x) ** 2 + d2 ** 2)  # distance between point of entry into water and a drowning. Feet.

timeSalvage = (L1 + L2 * coefSlowDownWater) / vs

print(f'If a lifeguard runs at the angle of 𝜃1 = {round(float(directionSand))}',
      f', he will reach the drowning in {timeSalvage:0.1f} seconds.')