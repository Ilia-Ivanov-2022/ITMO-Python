"""
laboratory job Basics

data types, input/ output, calculations, Math module.

@author: ilia.ivanov@outlook.com

Model module: calculations
"""

import math

# Constants

FEET_PER_YARD = 3
FEET_PER_MILE = 5280
SEC_PER_HOUR = 3600
"""
initializing a tuple
model_data[0]   shortest dist Lifeguard - shoreline, yards
model_data[1]   shortest dist shoreline - Drowning, feet
model_data[2]   offset Lifeguard - Drowning along shoreline, yards
model_data[3]   running speed over sand, mph
model_data[4]   coefficient of speed slowing down in water
model_data[5]   angle at which Lifeguard runs to Drowning, °
"""
model_data = (0.0, 0.0, 0.0, 0.0, 0, 0.0)

# Function

def calc_run_time(mdata):
    """
    calc_run_time receives a tuple consisting of 6 elements and returns a float
    """
    # offset Lifeguard - water entry point along waterline
    offset_onshore = (mdata[0] * FEET_PER_YARD) * math.tan(mdata[5] * math.pi / 180)
    # shortest distance Lifeguard - water entry point
    run_over_sand = math.sqrt(offset_onshore ** 2 + (mdata[0] * FEET_PER_YARD) ** 2)
    # shortest distance water entry point - Drowning
    swim = math.sqrt(((mdata[2] * FEET_PER_YARD) - offset_onshore) ** 2 + mdata[1] ** 2)
    return (run_over_sand + swim * mdata[4]) / (mdata[3] * FEET_PER_MILE/SEC_PER_HOUR)
