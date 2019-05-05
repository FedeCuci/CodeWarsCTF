import random
import string

def randomPassword(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits # Store digits and letters in ASCII
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# def main():

#     passwords = []

#     # Generate random password
#     for i in range(19):
#         p_random = randomPassword()
#         passwords.append(p_random)

#     # joined = '\n'.join(passwords)

#     with open('.passwords', 'x+') as f_passwords:
#         # f_passwords.write(str(passwords))
#         f_passwords.write(joined)
#         # lines = f_passwords.readlines()

# if __name__ == '__main__':
#     main()
#os.system('chmod 100 .passwords')
