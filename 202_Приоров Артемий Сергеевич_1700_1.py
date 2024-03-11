import csv

with open('vacancy.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))  # считываем данные с файла
    comp = {}
    for i in reader[1:]:  # Обработка данных
        if i[-1] not in comp:
            comp[i[-1]] = int(i[0])
        else:
            comp[i[-1]] = max(comp[i[-1]], int(i[0]))

with open('vacancy_new.csv', 'w', newline='', encoding='utf-8') as f:
    a = []
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['company', 'role', 'Salary'])  # записываем данные в файл vacancy_new.csv
    k = 0
    for i in reader[1:]:
        if int(i[0]) == comp[i[-1]]:
            writer.writerow([i[-1].strip(' '), i[3], i[0]])
            a.append(int(i[0]))
    for i in reader[1:]:
        if int(i[0]) == max(a):
            k += 1
            print(f'{i[-1]}-{i[-2]}-{i[0]}')
        if k == 3:
            break
