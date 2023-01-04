"""
Lab 5. Functions. Main modul
"""
import lab_5
# Naming the players
igrok1 = lab_5.player_name_input(1)
igrok2 = lab_5.player_name_input(2)
# win and score counters
win_igrok1: int = 0
win_igrok2: int = 0
score_igrok1: int = 0
score_igrok2: int = 0

# Roll the dice
for i in range(5):
	score1 = lab_5.roll_the_dice(igrok1)
	score_igrok1 += score1
	score2 = lab_5.roll_the_dice(igrok2)
	score_igrok2 += score2
	if score1 > score2:
		win_igrok1 += 1
		print(f"Выиграл {igrok1}")
	elif score2 > score1:
		win_igrok2 += 1
		print(f"Выиграл {igrok2}")
	else: print('Ничья')

# Results output
if win_igrok1 > win_igrok2:
	print(f"По результатам сета выиграл {igrok1} {win_igrok1} раз,"
		  f" с общим счетом {score_igrok1}")
elif win_igrok2 > win_igrok1:
	print(f"По результатам сета выиграл {igrok2} {win_igrok2} раз,"
		  f" с общим счетом {score_igrok2}")
elif win_igrok1 == win_igrok2 and score_igrok1 > score_igrok2:
	print(f"По результатам сета выиграл {igrok1}"
		  f" по разнице в счете {score_igrok1 - score_igrok2}")
else: print(f"По результатам сета выиграл {igrok2}"
		  f" по разнице в счете {score_igrok2 - score_igrok1}")
