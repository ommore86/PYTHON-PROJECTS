import mysql.connector
from mysql.connector import Error
# from DATABASE_CONFIG import *

class ATM_Manager():

    def __init__(self) -> None:
        """Initialize the database connection"""
        self.connect()
    
    def connect(self):
        """Connect to the database"""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=1234,
            database="atm_db"
        )
        self.cursor = self.db.cursor()

    def register_users(self, userID, surname, fstname, homeadd, phonenum):
        """Register a new user to the database"""
        self.connect()
        try:
            query = "INSERT INTO users (userID, surname, fstname, homeadd, phonenum) VALUES (%s, %s, %s, %s, %s)"
            vars = (userID, surname, fstname, homeadd, phonenum)
            self.cursor.execute(query, vars)
            self.db.commit()
            self.db.close()
        except Error as e:
            print(f"Failed to insert record into MySQL table {e}")


    def register_account(self, userID, userpasswd, balance):
        """Register a new account to the database"""
        self.connect()
        try:
            query = "INSERT INTO accounts (acctype, userID, balance, withdrawal_limit, withdrawal_freq, userpasswd) VALUES (%s, %s, %s, %s, %s, %s)"
            vars = ("savings", userID, balance, 20000,10, userpasswd)
            self.cursor.execute(query, vars)
            self.db.commit()
            self.db.close()
        except Error as e:
            print(f"Failed to insert record into MySQL table {e}")
            

    def login_account(self, userID, userpasswd):
        """Login an account by checking if the userID and password is correct and return the account number"""
        self.connect()
        try:
            self.db.commit()
            query = f"SELECT account_no FROM accounts WHERE userID = %s AND userpasswd = %s"
            self.cursor.execute(query, (userID, userpasswd))
            result = self.cursor.fetchone()
            self.db.close()
            if result == None:
                return (False, "Invalid userID or password.")
            else:
                return (True, int(result[0]))
        except Error as e:
            return (False ,f"Failed to select record from MySQL table {e}")


    def view_one(self, table, condition, value):
        """View a record from a table"""
        self.connect()
        try:
            query = f"SELECT * FROM {table} WHERE {condition} = {value}"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.db.close()
            return result
        except Error as e:
            print(f"Failed to select record from MySQL table {e}")

    def view_user(self, userID):
        """View a user's details by calling view_one()"""
        return self.view_one("users", "userID", userID)
        
    def view_account(self, account_no):
        """View an account's details by calling view_one()"""
        return self.view_one("accounts", "account_no", account_no)
    
    def view_balance(self, account_no):
        """View an account's balance"""
        return self.view_one("accounts", "account_no", account_no)[3]
        
    def view_all_transactions(self, account_no):
        """View all transactions of an account"""
        self.connect()
        try:
            query = f"SELECT * FROM transactions WHERE account_no = {account_no}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.db.close()
            return result
        except Error as e:
            print(f"Failed to select record from MySQL table {e}")
    
    def view_day_transactions(self, account_no):
        """View all transactions of an account within the day"""
        self.connect()
        try:
            query = f"SELECT * FROM transactions WHERE account_no = {account_no} AND trans_date = CURDATE()"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.db.close()
            return result
        except Error as e:
            print(f"Failed to select record from MySQL table {e}")

    def withdraw(self, account_no, amount):
        """Check first if the amount to be withdrawn is within the limit and frequency"""
        # Get the transaction history of the account within the day and sum up the withdrawals
        transactions = self.view_day_transactions(account_no)
        total_withdrawals_amount = 0
        total_withdrawals_freq = 0
        for transaction in transactions:
            if transaction[0] == "Withdraw":
                total_withdrawals_amount += transaction[1]
                total_withdrawals_freq += 1

        # Check if the amount to be withdrawn is within the limit and frequency
        if amount > int(self.view_account(account_no)[3]):
            return "Insufficient funds."
        elif total_withdrawals_freq > self.view_account(account_no)[5]:
            return f"Exceeded withdrawal frequency for today. You're only allowed to withdraw {self.view_account(account_no)[5]} times today."
        elif total_withdrawals_amount > self.view_account(account_no)[4]:
            return f"Exceeded withdrawal limit for today. Your withdrawal limit for today is {self.view_account(account_no)[4]}."
        elif total_withdrawals_amount + amount > self.view_account(account_no)[4]:
            return f"Amount will exceed withdrawal limit for today. Your withdrawal limit for today is {self.view_account(account_no)[4]}."
        else:
            self.connect()
            try:
                # Updating the balance of the account
                query = f"UPDATE accounts SET balance = balance - {amount} WHERE account_no = {account_no}"
                self.cursor.execute(query)
                self.db.commit()
                
                # Adding the transaction into the transaction history
                query = "INSERT INTO transactions (account_no, trans_date, trans_type, amount) VALUES (%s, CURDATE(), %s, %s)"
                vars = (account_no, "Withdraw", amount)
                self.cursor.execute(query, vars)
                self.db.commit()
                self.db.close()
                
                return ("Done",f"You can withdraw {self.view_account(account_no)[5] - total_withdrawals_freq} more today.")
            except Error as e:
                return (f"Failed to update record in MySQL table {e}")
    
    def deposit(self, account_no, amount):
        """Deposit money into an account and add into the transaction history"""
        self.connect()
        try:
            # Updating the balance of the account
            query = f"UPDATE accounts SET balance = balance + {amount} WHERE account_no = {account_no}"
            self.cursor.execute(query)
            self.db.commit()
            
            # Adding the transaction into the transaction history
            query = "INSERT INTO transactions (account_no, trans_date, trans_type, amount) VALUES (%s, CURDATE(), %s, %s)"
            vars = (account_no, "Deposit", amount)
            self.cursor.execute(query, vars)
            self.db.commit()
            self.db.close()
            
            return "Done"
        except Error as e:
            print(f"Failed to update record in MySQL table {e}")       