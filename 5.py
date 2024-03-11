import csv

with open('vacancy.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]  # считываем данные с файла
    hash = {}
    maxVac = {}
    request = input()
    for i in reader:
        if i[-1] == request:
            print(f'{i[-1]}-{i[0]}-{i[1]}')
        if i[-1] not in hash:
            hash[i[-1]] = [i[3]]
            maxVac[i[-1]] = 1
        else:
            hash[i[-1]].append(i[3])
            maxVac[i[-1]] += 1
    print('Otis Worldwide')
