# R-Code Project: the game project for Metropolia IT Software 1

R-Code Project is a flight-simulator puzzle game prototype created by Giselle Altamiranda, Tingyu Pan, Pawanrat Santiyanon, and Binchi Zhou, first year students from Metropolia University of Applied Sciences. R-Code project is the final project of the course Software 1. 

This game program uses python as the main programming language. The project database is based on the flight_game database provided by the course lecturers. The project team redesigned and named the database as "crime_game". The Python program communicate the database through MySQL driver.

## Story and background

The story of R-Code project unveils in the fictional future, where the global industries are under the monopoly of a conglomerate called Conta Mega Inc. Behind the glory of the thriving Conta Mega Inc. lies a conspiracy which only a few people are aware of: Conta Mega Inc. has been secretly disposing Ricina, a toxic byproduct from Conta Mega Inc.’s affiliated factories. To hide their conducts from the public, Conta Mega Inc. has been randomly dropping a fraction of this toxic substance around the world, one country at a time. According to the ongoing investigation, five portions of Ricina have been disposed at five different locations so far. 

The player is a special agent and environment specialist from the Interpol. The player is asked to investigate the case, track the location of the substances, and eventually arrest Conta Mega Inc.’s toxic disposal team and press charges before Ricina pollutes every corner of the planet Earth.

## Install and Run

Before running the game, you need to download the game database to you local computer.

* Step 1: Clone the project code to you local computer. 
* Step 2: Download a database management system if it's not yet ready on your machine. We recommend using [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.3.0&os=windows&cpu=x86_64&pkg=msi&m=xtom_tal).
* Step 3: Go to your SQL console, input pass word, and execute the following command:
  * `create database crime_game;`
  * `use crime_game;`
  * `source` *the path to crime_game.sql*;
* Step 4: Change the password of database connection in db_functions.py to your own password.

Now you shall be able to run the main program.

## How to play

