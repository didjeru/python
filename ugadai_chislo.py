import random

print('Угадай число от 1 до 100:')
count_try = 0
number_min, number_max = 1, 100
comp_number = random.randint(number_min, number_max)

print(f'Ваше число: {comp_number} ?')
while True:
    user_answer = input()
    count_try = count_try+1
    if user_answer == '=':
        print(f'ПОБЕДА!!! c {count_try} попытки' )
        break
    elif user_answer == '>':
        try:
          number_min = comp_number+1
          comp_number = random.randint(number_min, number_max)
          print(f'Ваше число: {comp_number} ?')
        except ValueError:
          print('Вы ошиблись')
          break
    elif user_answer == '<':
        try:
          number_max = comp_number-1
          comp_number = random.randint(number_min, number_max)
          print(f'Ваше число: {comp_number} ?')
        except ValueError:
          print('Вы ошиблись')
          break
    else: print('Вы ввели неверный знак,')
