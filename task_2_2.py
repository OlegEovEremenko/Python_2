# Практическое задание. Задача №2

homework_list = ['в', '5', 'часов', '17', 'минут',
                 'температура', 'воздуха', 'была', '+5',
                 'градусов']

result = []

for el in homework_list:
    if el.isdigit():
        num = int(el)
        result.extend(['"', f'{num:02d}', '"'])
    elif el.startswith('-') or el.startswith('+') and el[1:].isdigit():
        num = int(el[1:])
        result.extend(['"', f'{el[0]}{num:02d}','"'])
    else:
        result.append(el)


print(result)
sentence = ' '.join(result).strip()
print(sentence)