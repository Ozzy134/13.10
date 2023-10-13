import re

def check_password(password):
    pattern = re.compile(r'^(?=.*[0-9])(?=.*[*#-])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z*#-]{8}$')
    if pattern.match(password):
        return 'Good'
    return 'Bad'

password_1 = 'dfsdG*11'
print(check_password(password_1))