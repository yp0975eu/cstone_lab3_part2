class Menu:
    '''for displaying main menu'''
    menu_options = ['create', 'find', 'update', 'delete', 'view all', 'quit']
    find_options = ['find by name', 'find by country', 'find by catches']

    def __init__(self):
        pass

    @staticmethod
    def display(options):
        #empty newline
        print()
        menu_num = 1
        for value in options:
            print(menu_num, value)
            menu_num += 1

    # for getting main menu selections
    @staticmethod
    def get_user_input(options):
        while True:
            try:
                selection = int(input('\n'))
                if selection not in range(len(options) + 1):
                    print("\nWas that a valid menu option?")
                    pass
                else:
                    return selection

            except ValueError as ve:
                print("\nWas that a number?")

            except KeyboardInterrupt as ki:

                exit('Goodbye')

    # takes a list of juggler objects
    @staticmethod
    def print_results(results):
        if len(results) == 0:
            print('We got nothing. Sorry.')
        else:
            for juggler in results:
                print("ID: {0}\t name: {1}\t country: {2}\t catches: {3}"
                      .format(juggler.id, juggler.name, juggler.country, juggler.catches))


class Dialogs:
    '''for handling cases when we need to interact with user and get input'''
    @staticmethod
    def show_create():

        name = input('Enter name\n')

        country = input('Enter country\n')

        catches = Dialogs.get_int_input('Enter number of catches\n')

        return {'name':name, 'country':country, 'catches':catches}

    @staticmethod
    def show_update():

        id = Dialogs.get_int_input('Enter record ID\n')
        name = Dialogs.get_string_input("Enter name\n")
        country = Dialogs.get_string_input("Enter country\n")
        catches = Dialogs.get_int_input("Enter number of catches\n")
        return {'id':id, 'name':name, 'country':country, 'catches': catches}

    @staticmethod
    def show_delete():
        record_id = Dialogs.get_int_input('Enter record ID to delete\n')
        return {'id': record_id}

    @staticmethod
    def get_string_input(message):
        while True:
            try:
                search_string = input(message)
                return search_string
            except ValueError as ve:
                print('Find by name error')

    @staticmethod
    def get_int_input(message):
        while True:
            try:
                number_input = int(input(message))
                return number_input

            except ValueError as ve:
                print("\nWas that a number?\n")

