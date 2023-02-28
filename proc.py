import datetime
import random
# создание списка из CSV файла
def create_note():
    data = []
    fields = ["Идентификатор", "Заголовок", "Тело заметки", "Дата редактирования"]
    with open("notes.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    file.close()
    return data

#создание нового ID
def new_id():
    n = str(random.randint(1001, 9999)) #создаем случайный ID
    for i in create_note(): #проверяем наличие данного ID в нашем списке
        if i['Идентификатор'] == n:
            n = random.randint(1001, 9999)
        else:
            return str(n)

#Добавление заметки
def add_note():
    new_titles = str(input("Введите заголовок: ").title())
    new_body = str(input("Введите тело: ").title())
    now = datetime.datetime.now()
    new_all = new_id() + ',' + new_titles + ',' + new_body + ',' + str(now)
    with open("notes.csv", "a", encoding="utf-8") as file:
        file.write(new_all)
        file.write('\n')
        file.close()
    print('Заметка успешно сохранена')


# чтение списка
def read_csv():
    my_str = ''
    count = 0
    for i in create_note():
        my_str = str(i)
        my_str2 = my_str.replace(":", '-', -1)
        my_str3 = my_str2.replace("'", '', -1)
        my_str4 = my_str3.replace("{", '', -1)
        my_str5 = my_str4.replace("}", '', -1)
        count += 1
        print(f'{count}: {my_str5}')
        print("_" * (5 + len(my_str5)))


# какую заметку ищем:
def what_note():
    wt = str(input("введите заголовок: ").title())
    return wt

#редактирование заметки
def edit_note():
    wt = str(input("введите заголовок: ").title())
    data = []
    datatmp = []
    count = 0
    e = 0
    fields = ["Идентификатор", "Заголовок", "Тело заметки",
              "Дата редактирования"]
    with open("notes.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
            count += 1
# создаем новый списо, удаляя все данные выбранной заметки, но при этом сохранем ИДЕНТИФИКАТОР
    id = []
    for i in data:
        e += 1
        if i['Заголовок'] == wt:
            print(i)
            id.append(i['Идентификатор'])

        else:
            datatmp.append(i)
        file.close()
    with open("notes.csv", 'w', encoding='utf-8') as file:
        for i in datatmp:
            old_id = i['Идентификатор']
            old_titles = i['Заголовок']
            old_body = i["Тело заметки"]
            now = datetime.datetime.now()
            new_all = old_id + ',' + old_titles + ',' + old_body + ',' + str(
                now)
            file.write(new_all)
            file.write('\n')
        file.close()
    new_titles = str(input("Введите новый заголовок: ").title())
    new_body = str(input("Введите новое тело: ").title())
    now = datetime.datetime.now()
# добавляем обновленные данные заметки и старый идентификатор в новый файл
    new_all = id[0] + ',' + new_titles + ',' + new_body + ',' + str(now)
    with open("notes.csv", "a", encoding="utf-8") as file:
        file.write(new_all)
        file.write('\n')
        file.close()
    print('Заметка успешно обновлена')
    id.remove(id[0])


# удаление заметки
def remove_note():
    wt = str(input("введите заголовок: ").title())
    data = []
    datatmp = []
    count = 0
    e = 0
    fields = ["Идентификатор", "Заголовок", "Тело заметки",
              "Дата редактирования"]
    with open("notes.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
            count += 1
#создаем новый список, исключая удаленную заметку
    for i in data:
        e +=1
        if i['Заголовок'] == wt:
            print(i)
        else:
            datatmp.append(i)
        file.close()
# добавляем новый список в файл
    with open("notes.csv", 'w', encoding='utf-8') as file:
        for i in datatmp:
            old_id = i['Идентификатор']
            old_titles = i['Заголовок']
            old_body = i["Тело заметки"]
            now = datetime.datetime.now()
            new_all = old_id + ',' + old_titles + ',' + old_body + ',' + str(now)
            file.write(new_all)
            file.write('\n')
        file.close()


# Сохранение файла в формате txt
def save_txt():
    my_file = open("Output.txt", "w+")
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open("notes.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            create_note().append(record)
            my_file.write(line)
    my_file.close()
    file.close()
    print('Готово')


