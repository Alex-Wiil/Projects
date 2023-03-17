from random import*
answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'] 

def answer_question(answers):
  return randint(0, len(answers) - 1)

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
flag = True
name = input('\nКак тебя зовут? ')
print('\nПривет ' + name)

while True:
  if flag == False:
    break
  else:
    question = input('\nЗадай свой вопрос: ')
    print(answers[answer_question(answers)])
  
  
  while True:
    choice = input('\nХочешь задать ещё вопрос? ')
 
    if choice.lower() == 'нет':
      flag = False
      print('\nВозвращайся если возникнут вопросы!')
      break
    elif choice.lower() == 'да':
      break
    else:
      print('Ответь "да" или "нет" ')
      continue