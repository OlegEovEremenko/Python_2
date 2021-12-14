# Практическое задание. Задача № 4

homework_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for phrase in homework_list:
    name = phrase.split(' ')
    print(f'Привет, {name[-1].capitalize()}!')
