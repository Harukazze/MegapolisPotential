import csv

with open('vacancy.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]  # считываем данные с файла
    printed = False
    request = input()
    while request != 'None':
        printed = False
        for i in reader:
            if i[-1] == request:
                print(f'В {i[-1]} найдена вакансия:{i[-2]}.З/п составит:{i[0]}')  # Выводим доступные вакансии
                printed = True
        if not printed:
            print('К сожалению ничего не удалось найти')  # сообщение, если ничего не удалось найти
        request = input()  # запрашиваем компанию, в которой хотим найти вакансию
