import re

pattern = re.compile(r"[A-Za-z0-9@#$%]{8,}")

while True:
    password = input('Please input password that contain letters, numbers, symbols $%#@, and at least 8 char long: ')
    check = pattern.fullmatch(password)
    try:
        if password == check.group():
            print('Your password accepted!')
            break
    except AttributeError:
        print('Please input password in right format')
        continue

