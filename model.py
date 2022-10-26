import controller

phone_book = []
path = 'data/'


def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path 
    path += file

def open_file():
    global path 
    global phone_book
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)
        

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book  
    phone_book [int(id)][int(choise)] = value

def delete_contact(id):
    global phone_book
    phone_book.pop(id)

def find_contact(word):
    global phone_book
    for i in (phone_book):
        if word in i:
            return(i)
            
    
    
