from getpass import getpass
import hashlib

def registration():
	f_name = input("Enter First Name: ")
	l_name = input("Enter Last Name: ")
	employee_id = input("Enter Employee ID: ")


	# check database for user
	query = "SELECT * FROM Employees WHERE id=%s AND f_name=%s AND l_name=%s"
	cursor = connection.cursor()
	cursor.execute(query, employee_id, f_name, l_name)
	records = cursor.fetchone()

	# check if user is an employee
	if records == NULL:
		print("You are not an employee. You cannot register.")
		return

	# check if user is registered
	if records["has_registered"] == 1:
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
	pass_query = "UPDATE Employees SET password=%s WHERE id=%s"
	cursor.execute(pass_query, hashed_pass.hexdigest(), employee_id)
	connection.commit()


	print("Registration Successful!")
	return
