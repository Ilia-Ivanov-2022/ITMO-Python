"""
Standard library modules
"""
import random
from statistics import median, mean, stdev

# Creating 10 integers my_list
my_list = []
for i in range(10):
	my_list.append(random.randint(0, 100))
print('My list of 10 integers:', my_list)

# Testing my_sum_numbers method against python sum method.
def my_sum_numbers(obj):
	"""
	:param object: list of integers
	:return: sum of integers in the list
	"""
	sum_obj = 0
	for item in obj:
		sum_obj += item
	return sum_obj
# Python sum method
if sum(my_list) == my_sum_numbers(my_list):
	print('Sum of my_list:', sum(my_list))

print('Average:', mean(my_list))
print('Median:', median(my_list))
print('Standard deviation:', stdev(my_list))
