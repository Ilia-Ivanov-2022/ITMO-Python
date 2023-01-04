"""
Branching and loop operators
"""
from random import randint
import time
# Branching
#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
# win and score counters
win_igrok1: int = 0
win_igrok2: int = 0
score_igrok1: int = 0
score_igrok2: int = 0
# Добавление цикла
for i in range(5):
	#Моделирование бросания кубика первым играющим
	print('Кубик бросает', igrok1)
	time.sleep(2)
	n1 = randint(1, 6)
	score_igrok1 += n1
	print('Выпало:', n1)
	#Моделирование бросания кубика вторым играющим
	print('Кубик бросает', igrok2)
	time.sleep(2)
	n2 = randint(1, 6)
	score_igrok2 += n2
	print('Выпало:', n2)

	#Определение результата (3 возможных варианта)
	if n1 > n2:
		win_igrok1 += 1
		print('Выиграл:', igrok1)
	elif n1 < n2:
		win_igrok2 += 1
		print('Выиграл:', igrok2)
	else:
		print('Ничья')

# Found out the final winner
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
