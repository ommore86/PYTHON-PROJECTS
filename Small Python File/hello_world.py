import mysql.connector

print ("Hello World")

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "atm"
    )

mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE accounts RENAME COLUMN Pin_Hashcode to PIN_HASHcode")
sql = """DELETE FROM accounts WHERE ACC_NO=601010003917"""
mycursor.execute(sql)
mydb.commit()