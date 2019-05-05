<h1> CW_GAME </h1>

<h3> What is is: </h3>
CodeCTF is a project that aims to improve beginner's coding and problem solving skills. This is a collection of challenges taken directly from codewars that I think cover important and helpful concepts.

I give beginner computer science classes at my school and have originally made this project in order to help my students to improve their coding skills.

<h3> How it works: </h3>
The whole idea of this game is to add a bit more of a gameplay to codewars. These challenges could simply be solved on codewars directly, but I think that this way it's a bit more fun to play. In addition, I am planning to add some sort of ranking system in order to make it a bit more competitive.

<<<<<<< HEAD
I host these challenges on a VPS. Using the ```create_users.py script```, I create as many users as I need in order to give a private space on the VPS to all my students. This script will automatically create all the users for me with the right permissions and settings. I do this using newusers and python interchangeably. Note: every user has their own copy of the CTF.
=======
I host these challenges on a VPS. Using the ```create_users.py``` script, I create as many users as I need in order to give a private space on the VPS to all my students. This script will automatically create all the users for me with the right permissions and settings. I do this using newusers and python interchangeably. Note: every user has their own copy of the CTF.
>>>>>>> 5027eb1ac4a970c8e7b257c96226ea43f276b924

The challenges are all python scripts which contain a hard-coded link to the codewars challenge. The challenge must be solved directly on Codewars, since it will give the user the privilege and ability to use the codewars interface which already comes with all the unit-tests, solutions from other people, instructions etc.

After that, I use the codewars API to check if the user has succesfully completed the challenge and give a password to access the next level. The next level can only be accessed if in possession of this password.

<h3> How to setup the game (admin): </h3>
In order to setup the game, you need a VPS. In this VPS you need to install netcat in order to send the files over to your server. I would recommend putting all the contents of this repo in a folder and zip it. To send the files, I followed this link: https://nakkaya.com/2009/04/15/using-netcat-for-file-transfers/. After you have got the files on the server, you need to run ```create_users.py``` in order to create as many users as you want. (These are going to be the players of your game).

All the information about the users will be stored in the users.txt file. Now you can send usernames and passwords to all the people, that you want to play the game.

This is pretty much all there is to setup on the admin end, as ```create_users.py``` script will do everything for you.

<h3> How to play (client): </h3>
The first thing that needs to be done is have the credentials for a specific user. These must be given by the challenge administrator, which owns the vps. After that, you can login the server using SSH, like so:
ssh server_ip -l username Once inside the vps, you must navigate to codewars_ctf/challenges. From there the first script that needs to be run is the setup.py. This script, will ask you for your codewars username (no authentication yet) and it will be the username that all the challenge scripts will use in order to communicate to the codewars API and check whether you have actually completed the challenges.

From the client side, that is all that needs to be done. Now you can just run all the challenges in order and complete them all! There is actually a little vulnerability in the whole design of the challenges, and a way in which in theory you can get to the last level without completing all the ones before ;)
