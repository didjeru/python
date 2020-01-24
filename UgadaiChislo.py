import random

print('Угадай число от 1 до 100:')
count_try = 0
number_min, number_max = 1, 100
number = random.randint(number_min, number_max)

print(f'Ваше число: {number} ?')
while True:
    user_answer = input()
    count_try = count_try+1
    if user_answer == '=':
        print(f'ПОБЕДА!!! c {count_try} попытки' )
        break
    elif user_answer == '>':
        try:
          number_min = number+1
          number = random.randint(number_min, number_max)
          print(f'Ваше число: {number} ?')
        except ValueError:
          print('Вы ошиблись')
          break
    elif user_answer == '<':
        try:
          number_max = number-1
          number = random.randint(number_min, number_max)
          print(f'Ваше число: {number} ?')
        except ValueError:
          print('Вы ошиблись')
          break
    else: print('Вы ввели неверный знак')
