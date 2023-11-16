<h1> CW_GAME </h1>

<div align="center">

# Simple Gossip Implementation in Python

#### 🔧 Made with:
![](https://img.shields.io/badge/-Python-informational?style=flat&logo=Python&logoColor=white)

[What is this?](#whatisthis)
•
[How it works](#howitworks) 
•
[How to Set Up the Game (admin)](#howtosetupthegame)
•
[How to Play (client)](#howtoplay) 

</div>

## What is this?
CodeCTF is a project that aims to improve beginner's coding and problem-solving skills through hands-on practice. This is a collection of Python challenges taken directly from CodeWars, each of which covers important and helpful concepts in algorithmic thinking.

I give beginner computer science classes at my school and originally made this project in order to help my students improve their coding skills.

## How it works
The whole idea of this game is to add a bit more gameplay to Codewars. These challenges could simply be solved on codewars directly, but I think that this way is a bit more fun to play. In addition, I am planning to add some sort of ranking system in order to add a competition aspect to it.

I host these challenges on a VPS using `neoserver.site` a great and cheap VPS provider from Russia. Using the ```create_users.py script```, I create as many Linux users as I need in order to give a private space on the VPS to all my students. This script will automatically create all the Linux users for me with the right permissions and settings. I do this using the `newusers` command and `python` interchangeably. Note: Every user has their own copy of the CTF.

The challenges are all Python scripts that contain a hard-coded link to the Codewars challenge. The challenge must be solved directly on Codewars since it will give the user the privilege and ability to use the codewars interface, which comes with all the unit-tests, solutions from other people, instructions, etc.

After that, I use the Codewars API to check if the user has successfully completed the challenge and give them a password to access the next level on the VPS. The next level can only be accessed if you are in possession of this password. By adding this extra-layer of having to access the levels on the command line, it is my hope that students get familiar with using Linux. This idea is inspired by the [OverTheWire Bandit Challenges](https://overthewire.org/wargames/bandit/)

## How to setup the game (admin):
In order to set up the game, you need a VPS. In this VPS, you need to install `netcat` or `ssh` in order to send the files over to your server. I would recommend putting all the contents of this repo in a folder and zipping it, which will allow you to send all files at once. To send the files, [I followed these instructions](https://nakkaya.com/2009/04/15/using-netcat-for-file-transfers/). After you have the files on the server, you need to run `python create_users.py` in order to create as many users as you want. These are going to be the players in your game.

All the information about the users will be stored in the users.txt file. Now you can send usernames and passwords to all your students.

This is pretty much all there is to setup on the admin end, as the ```create_users.py``` script will do everything for you.

## How to play (client):
The first thing that needs to be done is to have the credentials for a specific user. These must be given by the challenge administrator, which owns the VPS. After that, you can login to the server using SSH, like so:
ssh ```server_ip -l username``` Once inside the VPS, you must navigate to ```codewars_ctf/challenges```. From there, the first script that needs to be run is `setup.py`. This script will ask you for your codewars username (no authentication yet) and it will be the username that all the challenge scripts will use in order to communicate with the codewars API and check whether you have actually completed the challenges.

From the client side, that is all that needs to be done. Now you can just run all the challenges in order and complete them all! There is actually a little vulnerability in the whole design of the challenges and a way in which, in theory, you can get to the last level without completing all the ones before. This is up to the player to find out and tinker with the system!
