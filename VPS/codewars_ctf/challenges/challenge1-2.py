# Challenge2.py
import json
import time
import os
import sys
import requests
import r

# Hey there, I see you are looking at the code :)
# What are you trying to find?
# A vulnerability perhaps?

with open('.passwords', 'r') as passwords:
        password = passwords.readlines()

try:
    if sys.argv[1].strip() != password[0].rstrip():
        print('Password is not correct')
        exit()
    elif sys.argv[1].strip() == password[0].rstrip():
        print('Challenge to complete: \n http://www.codewars.com/kata/55b42574ff091733d900002f/train/python \n Good luck! \n')

except IndexError:
    print('Please provide a password. Usage: python challenge1-2.py password')
    exit()

completed = input('\nPress enter once you think you are done')


with open('.username', 'r') as username_file:
    username = username_file.read()

# Loop to keep requesting data from API unitl challenge has been added to API
while True:

    print('Checking if challenge was completed...')

    time.sleep(3)
    # API request for completed challenges of user
    data = requests.get('https://www.codewars.com/api/v1/users/{}/code-challenges/completed'.format(username))

    # If successful
    if data.status_code == 200:
        # Get the data
        challenges_info = data.json()
    else:
        print('There was an error processing the data')
        break

    completed_challenges = {}
    ids = []

    # Loop over all the challenges of user (to review)
    for i in challenges_info['data']:
        ids.append(i['id'])

    # If the challenge id is in the API dictionary give password for next level
    if '55b42574ff091733d900002f' in ids:
        # Create a random string using the r.py file
        rp = r.randomPassword()
        with open('.passwords', 'a') as passwords:
            print('You have succesfully completed the challenge\n\
            Here is the password for the next level: {}'.format(rp))
            passwords.write(rp + '\n')
            break



