from database import DB
from menu import Menu, Dialogs

'''Simple application to insert update and delete records from a database'''


def run():
    # create tables
    db = DB()
    db.create_tables()
    data = None

    # loop
    while True:

        # display menu
        Menu.display(Menu.menu_options)

        # get user input
        selection = Menu.get_user_input(Menu.menu_options)

        if selection == 1:
            # returns a tuple with  ( name, country, number of catches )
            data = Dialogs.show_create()

            db.insert(data)

        if selection == 2:
            Menu.display(Menu.find_options)

            # get user input
            selection = Menu.get_user_input(Menu.find_options)
            if selection == 1:

                name = Dialogs.get_string_input('Enter name\n')

                data = db.find_by_name(name)

            elif selection == 2:

                country = Dialogs.get_string_input('Enter country\n')

                data = db.find_by_country(country)

            elif selection == 3:

                catches = Dialogs.get_int_input('Enter number of catches\n')

                data = db.find_by_catches(str(catches))

            else:

                data = db.get_all()

            Menu.print_results(data)

        # update a record
        if selection == 3:

            data = db.get_all()

            Menu.print_results_with_id(data)

            new_data = Dialogs.show_update()

            db.update_prepare(new_data)

        # delete a record
        if selection == 4:

            data = db.get_all()

            Menu.print_results_with_id(data)

            id_to_delete = Dialogs.show_delete()

            db.delete_prepare(id_to_delete)

            data = db.get_all()

            Menu.print_results_with_id(data)
        # exit program
        if selection == 5:
            db.close_connection()
            exit()

if __name__ == "__main__":
    run()
