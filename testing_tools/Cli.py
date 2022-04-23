from Core import *

def main():
    print('   _____                                  _____                                  _    _                                        \n'
          '  / ____|                                / ____|                                | |  (_)                   /\                  \n'
          ' | |      ___   _   _  _ __  ___   ___  | (___   _   _   __ _   __ _   ___  ___ | |_  _   ___   _ __      /  \    _ __   _ __  \n'
          ' | |     / _ \ | | | || \'__|/ __| / _ \  \___ \ | | | | / _` | / _` | / _ \/ __|| __|| | / _ \ | \'_ \    / /\ \  | \'_ \ | \'   \ \n'
          ' | |____| (_) || |_| || |   \__ \|  __/  ____) || |_| || (_| || (_| ||  __/\__ \| |_ | || (_) || | | |  / ____ \ | |_) || |_) |\n'
          '  \_____|\___/  \__,_||_|   |___/ \___| |_____/  \__,_| \__, | \__, | \___||___/ \__||_| \___/ |_| |_| /_/    \_\| .__/ | .__/ \n'
          '                                                         __/ |  __/ |                                            | |    | |    \n'
          '                                                        |___/  |___/                                             |_|    |_|    \n')

    print('You are logged in as a guest.')
    user_account = User(userName='guest')
    UniversalDataConnection(FileManager())


    while True:
        user_input = input('Please input a command:\n'
                          '     Add a course to your history: a\n'
                          '     Get a suggested list of courses for the next semester: g\n'
                          '     View current list of taken courses: v\n'
                          '     Quit: q\n')

        if user_input.lower() == 'a':
            add_course(account=user_account)

        elif user_input.lower() == 'v':
            view_courses(user_account)

        elif user_input.lower() == 'g':
            course_suggestion(user_account)

        elif user_input.lower() == 'q':
           quit(0)

        else:
            print('Command invalid.')


def add_course(account: User) -> None:
    """
    Helper function to encapsulate add course logic for command line interface.

    :param account: User account to add class to.
    :return: None
    """
    master = UniversalDataConnection.get_instance().data_connection.get_courselist()
    print('Please select a course from the following list of courses:')
    for key in master.course_dict.keys():
        print(key)
    selected_course = input()
    new_course = master.course_dict[selected_course]
    account.add_course(new_course)

def view_courses(account: User) -> None:
    print('Here are the current classes associated with your account:')
    for key in account.courseSet.course_dict.keys():
        print(key)

def course_suggestion(account: User) -> None:
    print('Here are the courses you should take next semester.')
    suggested_courses = account.suggest_courses(UniversalDataConnection.get_instance().data_connection.get_courselist())
    for course in suggested_courses:
        print(course.course_identifier)

if __name__ == '__main__':
    main()
