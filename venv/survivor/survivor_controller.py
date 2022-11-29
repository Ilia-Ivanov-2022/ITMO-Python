"""
laboratory job Basics

data types, input/ output, calculations, Math module.

@author: ilia.ivanov@outlook.com

Controller module: invokes methods and procedures in 'view' and 'model' modules.
"""

import survivor_view, survivor_model
# gets data from a user and stores in tuple
survivor_model.model_data = survivor_view.input_data()
# calculates results with above tuple as an argument
calc_data = survivor_model.calc_run_time(survivor_model.model_data)
# prints out results based on the above result and the tuple.
survivor_view.output_data(calc_data, survivor_model.model_data[5])
