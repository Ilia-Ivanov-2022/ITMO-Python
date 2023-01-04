"""
Lab 5. Functions
"""
from random import randint
import time

def player_name_input(player_number, result=None):
	"""
	The method receives number of a player whose name should be entered by user.
	Return name of the player.
	:param player_number: igrok1 = 1; igrok2 = 2
	:param result: return value. Initially equals None.
	:return: name of the player entered by a user.
	"""
	if player_number == 1:
		result = input('Enter first player name: ')
	elif player_number == 2:
		result = input('Enter second player name: ')
	else: print('Wrong number')
	return result

def roll_the_dice(player):
	"""
	Simulates dice for a given player
	:param player: Player number
	:return: dice result
	"""
	print('Кубик бросает', player)
	time.sleep(2)
	dice = randint(1, 6)
	print('Выпало:', dice)
	return dice
