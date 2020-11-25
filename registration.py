from getpass import getpass
import hashlib

def registration():
	f_name = input("Enter First Name: ")
	l_name = input("Enter Last Name: ")
	employee_id = input("Enter Employee ID: ")


	# check database for user
	sql_select_Query = "select * from Employees"
	cursor = connection.cursor()
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	found = false

	for row in records:
		if row[0] == employee_id and row[1] == f_name and row[2] == l_name:
			found = true
			break

	# check if user is an employee
	if found == false:
		print("You are not an employee. You cannot register.")
		return

	# check if user is registered
	if row[4] == 1:
		print("You are already registered. Please proceed to the login screen.")
		return


	password = getpass("Enter Password: ")
	confirm_pass = getpass("Confirm Password: ")

	while password != confirm_pass:
		print("Passwords do not match. Please retype your password.")
		password = getpass("Enter Password: ")
		confirm_pass = getpass("Confirm Password: ")

	hashed_pass = hashlib.sha256()
	hashed_pass.update(password)
	hashed_pass.digest()

	# save password in database
	cursor.execute('''
		INSERT INTO Employees (password)
		VALUES
		(hashed_pass.hexdigest()),
		''')


	print("Registration Successful!")
	return
