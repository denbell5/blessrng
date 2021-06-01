import re



def email_is_valid(email):
    email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(email_regex, email)):
        return True
    else:
        return False

def password_validation_errors(passwd):

    errors = []
    
    if len(passwd) < 6:
        errors.append('Password length should be at least 6 characters')
          
    if len(passwd) > 20:
        errors.append('Password length should be not be greater than 20 characters')
          
    if not any(char.isdigit() for char in passwd):
        errors.append('Password should have at least one numeral')
          
    if not any(char.isupper() for char in passwd):
        errors.append('Password should have at least one uppercase letter')
          
    if not any(char.islower() for char in passwd):
        errors.append('Password should have at least one lowercase letter')

    return errors


def username_is_valid(username: str):
    if (username.isalnum()):
        return True
    else:
        return False

def sign_up_validation_errors(email,password,username):
    errors = []
    if(not email_is_valid(email)):
        errors.append('Email is not valid')
    pwd_errors = password_validation_errors(password)
    if(pwd_errors != []):
        errors += pwd_errors
    if(not username_is_valid(username)):
        errors.append('Only word and numbers are allowed for usernames')

    return errors