def validate_username(username):
	if not username:
		return False
	if " " in username:
		return False
	return True


def validate_password(password):
	if len(password) < 8:
		return False
	if not any(char.isdigit() for char in password):
		return False
	if not any(char.isalpha() for char in password):
		return False
	if not any(char in "!@#$%^&*()_+=-`~[]{}|;:'\",.<>?/\\ " for char in password):
		return False
	return True
	

def validate_email(email):
	if "@" in email and "." in email:
		return True
	return False

	