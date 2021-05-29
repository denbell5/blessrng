import random, string


def generate_passwords(password_length, count):
    password_characters = string.ascii_letters + string.punctuation + string.digits
    passwords = []
    for password in range(count):
        temp = []
        for x in range (password_length):
            temp.append(random.choice(password_characters))
        password = ''.join(temp)
        passwords.append(password)
    return passwords