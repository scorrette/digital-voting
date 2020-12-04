# Digital Voting Project
#   Login Screen
#
#
# Author of login.py: Kris Caceres


# Prompt users to put their credentials (user,pw)
# Verify user identity by comparing their credentials with the stored ones in softawre's database
#   if successful, prompt user to 'Main Screen';
#   otherwise, display error message "credentials incorrect, try again"
import getpass

def prompt_login():
    # prompt users for credentials
    # call verify function
    # send user to main screen if successful
    user = getpass.getuser()
    try:
        p = getpass.getpass()
    except Exception as error:
        print('Error', error)
    else:
        print('Password entered')
        # maybe implement verification here
        verify_login


def verify_login(user, pw):
    # pass credentials here
    # check against database
    # send boolean and username to main screen?



    return True


# info passed to main scrreen is user id (username) and that might be it
# clear password