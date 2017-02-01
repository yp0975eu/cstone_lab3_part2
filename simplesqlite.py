from database import DB
from menu import Menu, Dialogs

'''Simple application to insert update and delete records from a database'''


def run():
    # create tables
    db = DB()

    # db.create_tables()
    data = None

    # loop
    while True:

        # display menu
        Menu.display(Menu.menu_options)

        # get user input
        selection = Menu.get_user_input(Menu.menu_options)
        # select
        if selection == 1:
            # returns a tuple with  ( name, country, number of catches )
            data = Dialogs.show_create()

            db.insert(data)

        # find
        if selection == 2:

            Menu.display(Menu.find_options)

            # get user input
            selection = Menu.get_user_input(Menu.find_options)

            if selection == 1:

                name = Dialogs.get_string_input('Enter name\n')

                results = db.find_by_name(name)

                # results obj
                Menu.print_results(results)

            elif selection == 2:

                country = Dialogs.get_string_input('Enter country\n')

                results = db.find_by_country(country)

                Menu.print_results(results)

            elif selection == 3:

                catches = Dialogs.get_int_input('Enter number of catches\n')

                results = db.find_by_catches(str(catches))

                Menu.print_results(results)

        # update a record
        elif selection == 3:

            data = db.get_all()

            Menu.print_results(data)

            new_data = Dialogs.show_update() #returns dictionary

            db.update(new_data)

        # delete a record
        elif selection == 4:

            data = db.get_all()

            Menu.print_results(data)

            id_to_delete = Dialogs.show_delete()

            db.delete(id_to_delete)

            data = db.get_all()

            Menu.print_results(data)

        # see all records
        elif selection == 5:
            results = db.get_all()
            Menu.print_results(results)

        # exit program
        elif selection == 6:
            db.close_connection()
            exit()

if __name__ == "__main__":

    try:
        run()
    except Exception as exc:
        print('something went wrong', exc)
