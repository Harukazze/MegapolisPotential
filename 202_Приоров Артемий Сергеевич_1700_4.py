import csv

with open('vacancy.csv', encoding='utf-8') as f:  # открываем файл
    reader = list(csv.reader(f, delimiter=';'))[1:]  # считываем данные с файла
    allJobs = {}
    for i in reader:
        if i[1] not in allJobs:
            allJobs[i[1]] = [int(i[0])]
        else:
            allJobs[i[1]].append(int(i[0]))
    for i in allJobs:
        allJobs[i] = round(sum(allJobs[i]) / len(allJobs[i]))  # считаем процент
    print(allJobs)
    for i in reader:
        i.append(f'{int(i[0]) / allJobs[i[1]] * 100}%')
print(reader)

with open('vacancy_procent.csv', 'w', newline='', encoding='utf-8') as f:  # создаём новый файл
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Salary', 'Work_Type', 'Company_Size', 'Role', 'Company', 'percent'])
    for i in reader:
        writer.writerow(i)
