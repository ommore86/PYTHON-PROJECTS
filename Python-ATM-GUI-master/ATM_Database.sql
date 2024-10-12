-- ATM DATABASE
CREATE DATABASE atm_db;

USE atm_db;

CREATE TABLE users(
	userID VARCHAR(10) PRIMARY KEY,
    surname VARCHAR(255) NOT NULL,
    fstname VARCHAR(255) NOT NULL,
    homeadd TEXT NOT NULL,
    phonenum VARCHAR(11) NOT NULL
);

CREATE TABLE accounts(
	account_no INT AUTO_INCREMENT PRIMARY KEY,
    acctype VARCHAR(255) NOT NULL,
    userID VARCHAR(10) NOT NULL,
    balance INT NOT NULL,
    withdrawal_limit INT NOT NULL,
    withdrawal_freq INT NOT NULL,
    userpasswd VARCHAR(255) NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE transactions(
	trans_type VARCHAR(10) NOT NULL,
    amount INT NOT NULL,
    trans_date DATE NOT NULL,
    account_no INT,
    FOREIGN KEY (account_no) REFERENCES accounts(account_no)
);