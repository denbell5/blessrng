import random, string


def generate_passwords(password_length, count, allow_special_characters):
    password_characters = string.ascii_letters + string.digits
    if (allow_special_characters):
        password_characters += string.punctuation
    passwords = []
    for password in range(count):
        temp = []
        for x in range (password_length):
            temp.append(random.choice(password_characters))
        password = ''.join(temp)
        passwords.append(password)
    return passwords