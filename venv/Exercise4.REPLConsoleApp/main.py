"""
Exercise 4. ITMO Python course. Group 124-16.

REPK Console App

Date 27.11.2022

@author: ilia.ivanov@outlook.com
"""

import func

while True:
	answer = input("Command ('loc', 'zip', 'dist', 'end') => ").lower()
	if answer == 'end':
		print('Done')
		break
	elif answer == 'loc':
		func.loc()
	elif answer == 'zip':
		func.zip()
	elif answer == 'dist':
		func.dist()
	else:
		print('Invalid command, ignoring')
