import random
import csv


# функция быстрой сортировки
def quick_sort(a):
    if len(a) <= 1:
        return a
    q = int(random.choice(a)[2])
    bigger = [n for n in a if int(n[2]) > q]
    lower = [n for n in a if int(n[2]) < q]
    e = [n for n in a if int(n[2]) == q]
    return quick_sort(lower) + e + quick_sort(bigger)


with open('vacancy.csv', encoding='utf-8') as f:  # открываем файл
    reader = list(csv.reader(f, delimiter=';'))
    data = reader[1:]
    sortedData = quick_sort(data)  # сортируем наши данные о количеству сотрудников
    for i in sortedData:
        if i[3] == 'классный руководитель':
            print(
                f'В компании {i[-1]} есть заданная профессия: классный руководитель, з/п в такой компании составит {i[0]}')
            break
