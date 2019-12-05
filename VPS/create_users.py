import os
import string
import random
import time
import subprocess

# Note: This script uses the 'newusers' command. More info: https://www.tecmint.com/create-multiple-user-accounts-in-linux/
# Users are created as 'user1', 'user2', 'user3'... the real names of the students are not used.

#Install PIP

# print('Updating system')
# os.system('apt-get update')

#print('Upgrading system')
#os.system('apt-get upgrade -y')
#os.system()
#os.system('apt-get install python3-pip -y')

# Generate a random password
def main():
    def randomPassword(stringLength=6):
        lettersAndDigits = string.ascii_letters + string.digits # Store digits and letters in ASCII
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    os.system('cd ..')
    user_amount = int(input('How many users? '))

    usernames = []

    n = 1
    # Create file to store user information
    with open('users.txt', 'x') as users:
        # Create as many users as specified in user_amount
        for i in range (1, user_amount+1):
            # users.write(f'user{i}:{randomPassword(8)}:{1000+user_amount}:{1000+user_amount}::/home/user{i}:/bin/bash\n')
            users.write('user{}:{}:{}:{}::/home/user{}:/bin/bash\n'.format(i, randomPassword(8), 1000+n, 1000+n, i))
            user = 'user{}'.format(i)
            usernames.append(user)
            n += 1
            # print(f'user{i}:{randomPassword(8)}:{100+user_amount}:{100+user_amount}::/home/user{i}:/bin/bash')

    print('Changing permission for users.txt\n')
    time.sleep(1)

    # Change permission of file so that only root can execute it
    os.system('chmod 0600 users.txt')
    time.sleep(1)

    # Create users with newusers command
    print('Creating all the users\n')
    os.system('sudo newusers users.txt')

    print('All users created succesfully\n')
    print('Changing permissions of users\n')
    time.sleep(1)

    m = 1

    # Change permissions of all users so they are not able to access each other
    for i in usernames:
        # os.system('chmod 0750 /home/{}'.format(i))

        os.system('cp -r codewars_ctf /home/{}/'.format(i))
        os.system('touch /home/{}/codewars_ctf/challenges/.username'.format(i))
        os.system('touch /home/{}/codewars_ctf/challenges/.passwords'.format(i))
        os.system('chmod -R 500 /home/{}/'.format(i))
        os.system('chmod 700 /home/{}/codewars_ctf/challenges/.username'.format(i))
        os.system('chmod 700 /home/{}/codewars_ctf/challenges/.passwords'.format(i))
        os.system('chmod 700 /home/{}/codewars_ctf/challenges/setup.py'.format(i))
        os.system('chown -R {}:{} /home/{}/'.format(i, 1000+m, i))



        # os.system('rm /home/{}/codewars_ctf/create_users.py.'.format(i))
        m += 1

    exit(0)

if __name__ == '__main__':
    main()

