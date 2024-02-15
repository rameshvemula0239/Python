import re

def validate_password(password):
    """
    Validates the password according to the given criteria.
    """
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        return True
    else:
        return False

def main_password_validation(passwords):
    """
    The main function that takes a list of passwords and prints the valid ones.
    """
    valid_passwords = [password for password in passwords.split(',') if validate_password(password)]
    print(','.join(valid_passwords))

# Example usage:
passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
main_password_validation(passwords)