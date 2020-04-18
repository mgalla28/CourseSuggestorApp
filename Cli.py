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
    user_account = User('guest')


    while True:
        user_input = input('Please input a command:\n'
                          '     Add a course to your history: a\n'
                          '     Get a suggested list of courses for the next semester: g\n'
                          '     View current list of taken courses: v\n'
                          '     Quit: q\n')

        if user_input.lower() == 'a':
            add_course(user_account)

        if user_input.lower() == 'v':
            view_courses(user_account)

        if user_input.lower() == 'g':
            suggest_courses(user_account)

        if user_input.lower() == 'q':
           quit(0)


def add_course(account: User) -> None:
    print('Not implemented yet.')

def view_courses(account: User) -> None:
    print('Not implemented yet.')

def suggest_courses(account: User) -> None:
    print('Not implemented yet.')

if __name__ == '__main__':
    main()
