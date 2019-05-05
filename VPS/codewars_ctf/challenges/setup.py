import subprocess
import requests
import json
import os

os.system('clear')

while True:
    # Ask for codewars username
    c_username = input('Codewars username: ')
    # Download user completed challenges
    data = requests.get('https://www.codewars.com/api/v1/users/{}'.format(c_username))

    # Check for errors
    if data.status_code == 404:
        print('Please enter a valid username')
    elif data.status_code == 200:

        # Get username of system
        # username = subprocess.check_output('whoami')
        # username = username.rstrip(b'\n')
        # username = username.decode('utf-8')

        # Store system username in hidden file in home directory
        # with open('/home/{}/.username'.format(username)) as username_file:
        with open('.username', 'w') as username_file:
            username_file.write(c_username)
            print('Codewars username added succesfully.')
        break
    else:
        print('Error code {}', data.status_code)

