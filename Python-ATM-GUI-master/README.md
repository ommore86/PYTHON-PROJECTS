<p align="center">
  <img src="https://github.com/AkunoCode/Python-ATM-GUI/blob/da8f440ca27fa62d292a05c4ea1e556ce0038cdb/Media/Golden_Mane.png" alt="Golden Mane - CP102 Finals Term Course Outcome Output">
</p>

This is a Python program for a banking/ATM system that uses MySQL database with mysql.connector module. The program uses tkinter customized with ttkbootstrap to create an appealing and interactive GUI for the user.

This project is the finals term course outcome requirement for the course "Computer Programming 2" (CP102) in the 2nd semester of academic year 2022-2023 in Manuel S. Enverga University Foundation. The goal of this project is to create a Python program that applies the principles of Object Oriented Paradigm (OOP) to perform CRUD operations in a database using Structured Query Language (SQL) with a Graphical User Interface (GUI) created using Tkiter.

## Project Details

### Repository Contents

The repository contains the following files and folders:

- **ATM_DB_Manager.py**: This file contains the class that handles the database. It includes various methods such as view, deposit, withdraw, login, register, and others.
- **ATM_GUI.py**: This is the GUI for the ATM system. It uses the tkinter library with ttkbootstrap and a custom theme. This is what is going to be used to navigate.
- **ATM_Database.sql**: This script contains the SQL statements to create the database and its tables.
- **Media**: This folder contains the image banners used in the program.

### How to Run the Program

To run the program, follow these steps:

1. Ensure that you have Python 3.x, tkinter, and ttkbootstrap installed on your machine.
2. Clone the repository to your local machine.
3. Create the MySQL database and tables by running the `atm_database.sql` script in your MySQL client.
4. Open the `ATM_DB_Manager.py` file and replace the `user` and `password` variables with your MySQL username and password.
5. Run the ttkcreator in your terminal and import the `atm_theme.py` located in the `Media` folder.
6. Run the `ATM_GUI.py` file to launch the GUI and start using the program.
