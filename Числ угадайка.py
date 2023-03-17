from random import*

def is_valid(number):
  if '.' in number or number.isdigit() == False or 1 > int(number) or int(number) > 100:
    return False
  else:
    return True
    
print('Добро пожаловать в числовую угадайку\nПопробуйте угадать число(от 1 до 100), которое я загадал.\n')
random_num = randint(1, 101)

while True:
  user_num = input('Введите число: ')
  if is_valid(user_num) == True:
    if int(user_num) < random_num:
      print('Ваше число меньше загаданного, попробуйте еще разок\n')
      continue
    elif int(user_num) > random_num:
      print('Ваше число больше загаданного, попробуйте еще разок\n')
      continue
    else:
      print('Вы угадали, поздравляем!')
      break
    
  else:
    print('А может быть все-таки введем целое число от 1 до 100?\n')
    continue