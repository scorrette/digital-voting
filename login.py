from getpass import getpass
import hashlib
import mysql.connector


def login():

	connection = mysql.connector.connect(
	    host = 'ss3010.rutgers-sci.domains',
	    user = 'ssrutge4_user1',
	    password = "yourpassword",
	    database = 'ssrutge4_ECE424'
	)

	employee_id = input("Enter Employee ID: ")

	# check if user exists
	query = "SELECT * FROM Employees WHERE id=%s"
	cursor = connection.cursor()
	cursor.execute(query, employee_id)
	records = cursor.fetchone()

	while records == NULL:
		print("Employee ID is not in the system. Please retype it.")
		employee_id = input("Enter Employee ID: ")

	# ask for password and hash it
	password = input("Enter Password: ")
	hashed_pass = hashlib.sha256()
	hashed_pass.update(password)
	hashed_pass.digest()

	# get corresponding hashed password from database
	stored_pass = records[3]

	# check if passwords match
	while hashed_pass.hexdigest() != stored_pass:
		print("Incorrect Password. Please retype your password.")
		password = getpass("Enter Password: ")
		hashed_pass = hashlib.sha256()
		hashed_pass.update(password)
		hashed_pass.digest()

	# get first name
	first_name = records[1]

	print("Login Successful!")
	cursor.close()
	connection.close()
	return employee_id, first_name
