# Nam Doan
# 1847037

words = input()
password = ''

for character in words:

    if (character == 'i'):
        password += '!'

    elif (character == 'a'):
        password += '@'

    elif (character == 'm'):
        password += 'M'

    elif (character == 'B'):
        password += '8'

    elif (character == 'o'):
        password += '.'

    else:
        password += character
password += "q*s"
print(password)
