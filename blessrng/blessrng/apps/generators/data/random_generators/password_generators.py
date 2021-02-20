import random, string


def generate_password(password_length):
    password_characters = string.ascii_letters + string.punctuation + string.digits
    password = []
    for x in range (password_length):
        password.append(random.choice(password_characters))
    return ''.join(password)
    