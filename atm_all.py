import random
import smtplib
import mysql.connector

class Atm:
    def new_Acc(self):
        print("\n", "Creating New Account".center(100, "-"))
        self.name = input("Enter your name: ")
        self.mob = int(input("Enter your mob. no.: "))
        self.email = input("Enter your email address: ")
        self.balance = int(input("Enter Opening Balance: "))

        try:
            while True:
                self.email_otp = random.randint(111111, 999999)
                self.email_otp = str(self.email_otp)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("omgmore2005@gmail.com", "hktpyqlbmztkywtk")           # password - hktpyqlbmztkywtk
                server.sendmail("omgmore2005@gmail.com", self.email, self.email_otp)
                server.close()
                print("\nVerify OTP sent to your email account...")
                self.email_ver = (input("Enter OTP: "))
                if self.email_otp == self.email_ver:
                    print("Verified Successfully...")
                    break
                else:
                    print("INCORRECT OTP!!!")
                    print("Trying again...")
        except:
            print("\nERROR in sending email!!!\nSkipping this process(Skipping email verification)...")

        while True:
            try:
                self.pin = int(input("\nSet PIN for your account(Only digits): "))
                self.pin1 = int(input("Re-enter PIN: "))
                if self.pin==self.pin1:
                    print("PIN set successfully!!!")
                    break
                else:
                    print("Incorrect PIN, Try Again...")
            except:
                print("Enter Valid PIN!!!, Only Digits are allowed\nTry Again...")

        self.sql = "INSERT INTO accounts(NAME, MOB_NO, BALANCE, EMAIL, PIN_HASHcode) VALUES(%s, %s, %s, %s, %s)"
        self.val = (self.name, self.mob, self.balance, self.email, self.pin)
        mycursor.execute(self.sql, self.val)
        mydb.commit()

        print("\nAccount created successfully!!!")
        print("Redirecting to Main Menu...")

    def login_Acc(self):
        print("\n", "Logging In Account".center(100, "-"))
        self.acc_no = int(input("Enter Acc. no. to Login: "))

        self.sql = """SELECT EMAIL FROM accounts WHERE ACC_NO=%s"""
        self.values = (self.acc_no)
        mycursor.execute(self.sql, (self.values,))
        self.email = mycursor.fetchone()[0]

        try:
            while True:
                self.email_otp = random.randint(111111, 999999)
                self.email_otp = str(self.email_otp)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("omgmore2005@gmail.com", "hktpyqlbmztkywtk")           # password - hktpyqlbmztkywtk
                server.sendmail("omgmore2005@gmail.com", self.email, self.email_otp)
                server.close()
                print("\nVerify OTP sent to your registered email account...")
                self.email_ver = (input("Enter OTP: "))
                if self.email_otp == self.email_ver:
                    print("Verified Successfully...")
                    break
                else:
                    print("INCORRECT OTP!!!, Trying again...")
        except:
            print("\nERROR in sending email!!!")
            print("Skipping this process(Skipping email verification)...")

        while True:
            print("".center(100, "-"))
            print("1. Deposite\t2. Withdraw\t3. Transfer money\t4. Change info\t5. Log Out")
            self.ch = int(input("Enter Choice: "))

            if self.ch==1:
                self.sql = """SELECT BALANCE FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.balance = mycursor.fetchone()[0]

                self.amount = int(input("Enter amount to deposit: "))
                self.new_balance = self.balance + self.amount

                self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.pin = mycursor.fetchone()[0]

                while True:
                    try:
                        self.pin1 = input("\nEnter PIN to complete process: ")
                        if self.pin==self.pin1:
                            self.sql = """UPDATE accounts SET BALANCE=%s WHERE ACC_NO=%s"""
                            self.values = (self.new_balance, self.acc_no)
                            mycursor.execute(self.sql, self.values)
                            mydb.commit()
                            print("₹{} has been deposited to your account successfully!!!".format(self.amount))
                            break
                        else:
                            print("PIN doesnt match, Try Again...")
                    except:
                        print("Enter Valid PIN!!!\nOnly Digits are allowed")

            elif self.ch==2:
                self.sql = """SELECT BALANCE FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.balance = mycursor.fetchone()[0]

                while True:
                    self.amount = int(input("Enter amount to withdraw: "))
                    self.new_balance = self.balance - self.amount

                    if self.amount<=self.balance:
                        self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                        self.values = (self.acc_no)
                        mycursor.execute(self.sql, (self.values,))
                        self.pin = mycursor.fetchone()[0]

                        while True:
                            try:
                                self.pin1 = input("\nEnter PIN to complete process: ")
                                if self.pin==self.pin1:
                                    self.sql = """UPDATE accounts SET BALANCE=%s WHERE ACC_NO=%s"""
                                    self.values = (self.new_balance, self.acc_no)
                                    mycursor.execute(self.sql, self.values)
                                    mydb.commit()

                                    print("₹{} has been withdrawn from your account successfully!!!".format(self.amount))
                                    break
                                else:
                                    print("PIN doesnt match, Try Again...")
                            except:
                                print("Enter Valid PIN!!!\nOnly Digits are allowed")
                        break        
                    else:
                        print("\nInsufficiet Balance!!! Try Again...\n")

            elif self.ch==3:
                self.sql = """SELECT BALANCE FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.balance = mycursor.fetchone()[0]

                self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.pin = mycursor.fetchone()[0]

                self.acc_no1 = int(input("\nEnter account no. where you want to transfer money: "))
                self.sql = """SELECT BALANCE FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no1)
                mycursor.execute(self.sql, (self.values,))
                self.balance1 = mycursor.fetchone()[0]

                self.amount = int(input("Enter amount to transfer: "))
                self.balance1 = self.balance1 + self.amount
                self.balance = self.balance - self.amount

                while True:
                    try:
                        self.pin1 = input("\nEnter PIN to complete process: ")
                        if self.pin==self.pin1:
                            self.sql = """UPDATE accounts SET BALANCE=%s WHERE ACC_NO=%s"""
                            self.values = (self.balance, self.acc_no)
                            mycursor.execute(self.sql, self.values)
                            mydb.commit()

                            self.sql = """UPDATE accounts SET BALANCE=%s WHERE ACC_NO=%s"""
                            self.values = (self.balance1, self.acc_no1)
                            mycursor.execute(self.sql, self.values)
                            mydb.commit()

                            print("₹{} has been transferred from your account successfully!!!".format(self.amount))
                            break
                        else:
                            print("PIN doesnt match, Try Again...")
                    except:
                        print("Enter Valid PIN!!!\nOnly Digits are allowed")

            elif self.ch==4:
                print("\n1. Name\t\t2. Mob no.\t3. Email\t4. PIN")
                self.ch=int(input("Enter what you want to change: "))

                if self.ch==1:
                    self.sql = """SELECT NAME FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.name = mycursor.fetchone()[0]

                    self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.pin = mycursor.fetchone()[0]

                    self.new_name = input("\nEnter new name: ")

                    while True:
                        try:
                            self.pin1 = input("\nEnter PIN to complete process: ")
                            if self.pin==self.pin1:
                                self.sql = """UPDATE accounts SET NAME=%s WHERE ACC_NO=%s"""
                                self.values = (self.new_name, self.acc_no)
                                mycursor.execute(self.sql, self.values)
                                mydb.commit()
                                print("""Your name has been changed to "{}" successfully!!!""".format(self.new_name))
                                break
                            else:
                                print("PIN doesnt match, Try Again...")
                        except:
                            print("Enter Valid PIN!!!\nOnly Digits are allowed")

                elif self.ch==2:
                    self.sql = """SELECT MOB_NO FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.mob = mycursor.fetchone()[0]

                    self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.pin = mycursor.fetchone()[0]

                    self.new_mob = int(input("\nEnter new mob. no.: "))

                    while True:
                        try:
                            self.pin1 = input("\nEnter PIN to complete process: ")
                            if self.pin==self.pin1:
                                self.sql = """UPDATE accounts SET MOB_NO=%s WHERE ACC_NO=%s"""
                                self.values = (self.new_mob, self.acc_no)
                                mycursor.execute(self.sql, self.values)
                                mydb.commit()
                                print("""Your Mob. no. has been changed to "{}" successfully!!!""".format(self.new_mob))
                                break
                            else:
                                print("PIN doesnt match, Try Again...")
                        except:
                            print("Enter Valid PIN!!!\nOnly Digits are allowed")

                elif self.ch==3:
                    self.sql = """SELECT EMAIL FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.mob = mycursor.fetchone()[0]

                    self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.pin = mycursor.fetchone()[0]

                    self.new_email = input("\nEnter new email: ")

                    while True:
                        try:
                            self.pin1 = input("\nEnter PIN to complete process: ")
                            if self.pin==self.pin1:
                                self.sql = """UPDATE accounts SET EMAIL=%s WHERE ACC_NO=%s"""
                                self.values = (self.new_email, self.acc_no)
                                mycursor.execute(self.sql, self.values)
                                mydb.commit()
                                print("""Your Email address has been changed to "{}" successfully!!!""".format(self.new_email))
                                break
                            else:
                                print("PIN doesnt match, Try Again...")
                        except:
                            print("Enter Valid PIN!!!\nOnly Digits are allowed")

                elif self.ch==4:
                    self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    self.mob = mycursor.fetchone()[0]

                    while True:
                        try:
                            self.pin1 = input("\nEnter Original PIN to start process: ")
                            if self.pin==self.pin1:
                                while True:
                                    try:
                                        self.pin = input("\nSet PIN for your account: ")
                                        self.pin1 = input("Re-enter PIN: ")
                                        if self.pin==self.pin1:
                                            self.sql = """UPDATE accounts SET PIN_HASHcode=%s WHERE ACC_NO=%s"""
                                            self.values = (self.pin, self.acc_no)
                                            mycursor.execute(self.sql, self.values)
                                            mydb.commit()
                                            print("PIN set successfully!!!")
                                            break
                                        else:
                                            print("PIN doesnt match, Try Again...")
                                    except:
                                        print("Enter Valid PIN!!!\nOnly Digits are allowed")

                                break
                            else:
                                print("PIN doesnt match, Try Again...")
                        except:
                            print("Enter Valid PIN!!!\nOnly Digits are allowed")

            elif self.ch==5:
                print("Logging you out...")
                break
            
            else:
                print("Enter proper choice\nTry Again...")

    def del_Acc(self):
        print("\n", "Deleting Account".center(100, "-"))
        self.acc_no = int(input("Enter account no. you wish to delete: "))
        self.email = input("Enter your email: ")
                    
        try:
            while True:
                self.email_otp = random.randint(111111, 999999)
                self.email_otp = str(self.email_otp)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("omgmore2005@gmail.com", "hktpyqlbmztkywtk")           # password - hktpyqlbmztkywtk
                server.sendmail("omgmore2005@gmail.com", self.email, self.email_otp)
                server.close()
                print("\nVerify OTP sent to your email account...")
                self.email_ver = (input("Enter OTP: "))
                if self.email_otp == self.email_ver:
                    print("Verified Successfully...")
                    break
                else:
                    print("INCORRECT OTP!!!")
                    print("Trying again...")
        except:
            print("ERROR in sending email!!!")
            print("Skipping this process(Skipping email verification)...")

        try:
            while True:
                self.sql = """SELECT PIN_HASHcode FROM accounts WHERE ACC_NO=%s"""
                self.values = (self.acc_no)
                mycursor.execute(self.sql, (self.values,))
                self.pin = mycursor.fetchone()[0]

                self.pin1 = input("\nEnter PIN to delete account: ")

                if self.pin==self.pin1:
                    self.sql = """DELETE FROM accounts WHERE ACC_NO=%s"""
                    self.values = (self.acc_no)
                    mycursor.execute(self.sql, (self.values,))
                    mydb.commit()
                    print("Account deleted successfully!!!\nRedirecting to main menu")
                    break
                else:
                    print("Error while deleting account")
                    continue
                    
        except:
            print("Enter Valid PIN!!!\nOnly Digits are allowed")


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "atm"
    )
    mycursor = mydb.cursor()
    '''
        Database Software: MySQL
        Table Name: accounts
        Column Name: ACC_NO(BIGINT)
                    NAME(VARCHAR(50))
                    MOB_NO(BIGINT)
                    BALANCE(INT)
                    EMAIL(varchar(50))
                    PIN_HASHcode(INT)

    '''

    obj = Atm()
    while True:
        try:
            print("\n", "Welcome to Om's ATM".center(100,"-"))
            print("Do you wish to...\n1. Create new account\n2. Login existing account\n3. Delete account\n4. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                obj.new_Acc()

            elif ch == 2:
                obj.login_Acc()

            elif ch==3:
                obj.del_Acc()

            elif ch == 4:
                print("\nExiting...")
                print("Thank You, Visit Again!!!")
                break

            else:
                print("Enter Proper Choice!\nTry Again...")
        except:
            print("Invalid Input!\nTry Again...")