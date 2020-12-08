import registration
import login
import mainScreen
import authenticatorFile
import Votecounter

def selection_menu(previous = None):
    print('Please select one of the following:')

    if previous == 'registration':
        print('1) Login')
        print('2) Quit')
    else:
        print('1) Register to vote')
        print('2) Login')
        print('3) Quit')

    return int(input('Enter a number: '))


print('Welcome to the ECE Voting application!\n')

choice = selection_menu()

while choice != 1 or choice != 2 or choice != 3:
    choice = input('That is not an option. Try again: ')

if choice == 1:
    registration.registration()
    choice += selection_menu('registration')

if choice == 2:
    eid, f_name = login.login()
    mainScreen.mainScreen(f_name, eid)

    choice += 1

if choice == 3:
    print('Goodbye!')
    quit()