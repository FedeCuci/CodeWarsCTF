# Challenge2.py
import json
import time
import os
import requests
import r

with open('.username', 'r') as username_file:
    username = username_file.read()

print('Challenge to complete: \n http://www.codewars.com/kata/5949481f86420f59480000e7/train/python \n  \n Good luck! \n')

completed = input('\nPress enter once you think you are done')

# Loop to keep requesting data from API unitl challenge has been added to API
while True:

    print('Checking if challenge was completed...')

    time.sleep(3)
    # API request for completed challenges of user
    data = requests.get('https://www.codewars.com/api/v1/users/{}/code-challenges/completed'.format(username))

    # If successful
    if data.status_code == 200:
        print
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
    if '5949481f86420f59480000e7' in ids:
        # Create a random string using the r.py file
        rp = r.randomPassword()
        with open('.passwords', 'a') as passwords:
            print('You have succesfully completed the challenge\n\
            Here is the password for the next level: {}'.format(rp))
            passwords.write(rp + '\n')
            break




