import view, model


def start():
    choise = 1
    while choise != 9:
        choise = view.show_menu()
        match(choise):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()
            case 2:
                pass 
            case 3:
                contact = view.input_contact()
                model.new_contact(contact)
            case 4:
                contact = view.input_change()
                model.change_contact(*contact)
            case 5:
                contact = view.input_delеtе()
                model.delete_contact(contact)
            case 6:
                word = view.input_find()
                contact = model.find_contact(word)
                print(contact)
                