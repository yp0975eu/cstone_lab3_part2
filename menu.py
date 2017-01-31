class Menu:

    menu_options = ['create', 'find', 'update', 'delete', 'quit']
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


    @staticmethod
    def print_results(data):
        if len(data) == 0:
            print('We got nothing. Sorry.')
        else:
            print(data)

    @staticmethod
    def print_results_with_id(data):
        if len(data) == 0:
            print('We got nothing. Sorry.')
        else:
            print('ID | Name | Country | Catches')
            for d in data:
                print('{0}{1}{2}{3}'
                      .format(str(d[0]).ljust(5),str(d[1]).ljust(7),str(d[2]).ljust(10),str(d[3]).ljust(10)))


class Dialogs:

    @staticmethod
    def show_create():

        name = input('Enter name\n')

        country = input('Enter country\n')

        catches = Dialogs.get_int_input('Enter number of catches\n')

        return name, country, catches

    @staticmethod
    def show_update():

        id = Dialogs.get_int_input('Enter record ID\n')
        name = Dialogs.get_string_input("Enter name\n")
        country = Dialogs.get_string_input("Enter country\n")
        catches = Dialogs.get_int_input("Enter number of catches\n")
        return id, name, country, catches

    @staticmethod
    def show_delete():
        id = Dialogs.get_int_input('Enter record ID to delete\n')
        return id

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

