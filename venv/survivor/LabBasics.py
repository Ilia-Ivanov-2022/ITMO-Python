"""
laboratory job Basics

data types, input/ output, calculations, Math module.

@author: ilia.ivanov@outlook.com
"""

import math

# Constants
FEET_PER_YARD = 3
FEET_PER_MILE = 5280
SEC_PER_HOUR = 3600

# Function

def calc_run_time(dist1: float, dist2: float, offset: float,
                  speed: float, coef: int, angle: str):
      offset_onshore = dist1 * math.tan(float(angle) * math.pi / 180)
      run_over_sand = math.sqrt(offset_onshore ** 2 + dist1 ** 2)
      swim = math.sqrt((offset - offset_onshore) ** 2 + dist2 **2)
      print(f'If a lifeguard runs at the angle of '
            f'𝜃1 = {round(float(angle))}',
            f', he will reach a drowning in '
            f'{((run_over_sand + swim * coef) / speed):0.1f} seconds.')

# Data input

d1 = float(input("Enter a shortest distance between the"
                 " Lifeguard and waterline in yards: ")) * FEET_PER_YARD
d2 = float(input("Enter a shortest distance between the drowning man and waterline in feet: "))
h = float(input("Enter a side offset along waterline between"
                " a lifeguard and a drowning in yards: ")) * FEET_PER_YARD
vs = float(input("Enter a lifeguard speed running in sand, mph: ")) * FEET_PER_MILE / SEC_PER_HOUR
coefSlowDownWater = int(input("Enter a coefficient of lifeguard slowing down in the water, n: "))
directionSand = input("Enter an angle of running over the sand direction, °: ")

# Invoke function
calc_run_time(d1, d2, h, vs, coefSlowDownWater, directionSand)