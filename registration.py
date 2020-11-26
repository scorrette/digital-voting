from getpass import getpass
import hashlib

def registration():
	first_name = input("Enter First Name: ")
	last_name = input("Enter Last Name: ")
	employee_id = input("Enter Employee ID: ")


	# check database for user
	query = "SELECT * FROM Employees WHERE id=employee_id AND f_name=first_name AND l_name=last_name"
	cursor = connection.cursor()
	cursor.execute(query)
	records = cursor.fetchall()
	found = false

	# check if user is an employee
	if records == null:
		print("You are not an employee. You cannot register.")
		return

	# check if user is registered
	if records["is_registered"] == 1:
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
	pass_query = "UPDATE Employees WHERE password=%s"
	cursor.execute(pass_query, hashed_pass.hexdigest())
	connection.commit()


	print("Registration Successful!")
	return
