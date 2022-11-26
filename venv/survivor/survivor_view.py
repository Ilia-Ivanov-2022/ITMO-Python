"""
laboratory job Basics

data types, input/ output, calculations, Math module.

@author: ilia.ivanov@outlook.com

View module: data input and output.
"""

def input_data():
    """ User data input. Returns a tuple containing 6 elements"""
    run = float(input("Enter a shortest distance between the"
                 " Lifeguard and waterline in yards: "))
    swim = float(input("Enter a shortest distance between the drowning"
                       " man and waterline in feet: "))
    offset_total = float(input("Enter a side offset along waterline between"
                " a lifeguard and a drowning in yards: "))
    run_speed = float(input("Enter a lifeguard speed running over sand, mph: "))
    coef_slow_down_water = int(input("Enter a coefficient of lifeguard"
                                  " slowing down in the water, n: "))
    direction_sand = float(input("Enter an angle of running over the sand direction, °: "))
    return (run, swim, offset_total, run_speed, coef_slow_down_water, direction_sand)

def output_data(data, angle):
    """
    Receives two floats as arguments and prints results.
    First argument is from model.calc_run_time
    Second is from tuple model_data[5]
    """
    print(f'If a lifeguard runs at the angle of '
            f'𝜃1 = {round(angle)}',
            f', he will reach a drowning in '
            f'{data:0.1f} seconds.')
