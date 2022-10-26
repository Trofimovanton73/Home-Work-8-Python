def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')

    choise = int(input('Введите пункт меню: '))
    return choise 

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Ведите ФИО контакта')
    phone_contact = input('Ведите телефон контакта')
    comment_contact = input('Ведите коментарий')
    return(name_contact, phone_contact, comment_contact)

def input_change():  
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choise = input('0-ФИО, 1 - телефон, 2 - коментарий, 3 - отмена: ' )
    Value = input('Введите изменения')
    return (id, choise, Value)

def input_delеtе():
    id =int(input('Введите номер контакта, который нужно удалить: '))
    return (id)

def input_find():
    letters = input('Введите id или имя или фамилию или телефон(можно часть): ')
    return (letters)


    









