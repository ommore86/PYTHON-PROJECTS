import tkinter as tk
import ttkbootstrap as ttk
from ATM_DB_Manager import ATM_Manager as ATM_DB
from tkinter import messagebox as msg

class ATM_Login(ttk.Window):
    def __init__(self, title, size, theme):
        super().__init__(title=title, size=size, themename=theme)
        self.size = size
        self.center_window()
        self.resizable(False, False)
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 15, 'bold'))
        self.acc_no = None

        self.atm_db = ATM_DB()

        title_image = tk.PhotoImage(file="Media/Golden_Mane_Title.png")
        # Resize
        title_image = title_image.subsample(3,3)
        title_label = ttk.Label(self, image=title_image)
        title_label.image = title_image
        title_label.pack(side="top", anchor='center')

        # UserID Label
        self.userID_label = ttk.Label(self, text="User ID", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.userID_label.pack(side="top",padx=20,pady=10, anchor='center')

        # UserID Entry
        self.userID_var = tk.StringVar()
        self.userID_entry = ttk.Entry(self, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.userID_var)
        self.userID_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # Password Label
        self.password_label = ttk.Label(self, text="Password", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.password_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Password Entry
        self.userpassword_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", show="*", textvariable=self.userpassword_var)
        self.password_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # button frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side="top",padx=20,pady=10, anchor='center')

        # Login Button
        self.login_button = ttk.Button(self.button_frame, text="Login", command=lambda: self.login_function(self.userID_var.get(), self.userpassword_var.get()))
        self.login_button.pack(side="left",padx=20,pady=10, anchor='center', ipadx=10, ipady=10)

        # register Button
        self.register_button = ttk.Button(self.button_frame, text="Register", command=lambda: self.register_function())
        self.register_button.pack(side="left",padx=20,pady=10, anchor='center', ipady=10)

        
        self.mainloop()

    def login_function(self, user_id, password):
        self.acc_no = self.atm_db.login_account(user_id, password)
        
        # Clear the entry widgets
        self.userID_var.set("")
        self.userpassword_var.set("")

        if self.acc_no[0]:
            self.acc_no = self.acc_no[1]
            self.iconify()
            ATM_GUI("ATM", (720, 500), self.acc_no)    
        else:
            msg.showerror("Login Failed", self.acc_no[1])
    
    def register_function(self):
        self.iconify()
        ATM_Register("Register", (700, 700))

    def center_window(self):
        window_width = self.size[0]
        window_height = self.size[1]
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")    


class ATM_Register(ttk.Toplevel):
    def __init__(self, title, size):
        super().__init__(title=title, size=size)
        self.size = size
        self.center_window()
        self.resizable(False, False)
        self.atm_db = ATM_DB()

        title_image = tk.PhotoImage(file="Media/Golden_Mane_Title.png")
        # Resize
        title_image = title_image.subsample(2,2)
        title_label = ttk.Label(self, image=title_image)
        title_label.image = title_image
        title_label.pack(side="top", anchor='center')

        body_frame = ttk.Frame(self)
        body_frame.pack(side="top",padx=10,pady=5, anchor='center')

        user_info_frame = ttk.Frame(body_frame)
        user_info_frame.pack(side="left",padx=10,pady=5, anchor='center')

        account_info_frame = ttk.Frame(body_frame)
        account_info_frame.pack(side="right",padx=10,pady=5, anchor='center')

        # Surname Label
        self.surname_label = ttk.Label(user_info_frame, text="Surname", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.surname_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Surname Entry
        self.surname_var = tk.StringVar()
        self.surname_entry = ttk.Entry(user_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.surname_var)
        self.surname_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # First Name Label
        self.fstname_label = ttk.Label(user_info_frame, text="First Name", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.fstname_label.pack(side="top",padx=20,pady=10, anchor='center')

        # First Name Entry
        self.fstname_var = tk.StringVar()
        self.fstname_entry = ttk.Entry(user_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.fstname_var)
        self.fstname_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # Home Address Label
        self.homeadd_label = ttk.Label(user_info_frame, text="Home Address", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.homeadd_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Home Address Entry
        self.homeadd_var = tk.StringVar()
        self.homeadd_entry = ttk.Entry(user_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.homeadd_var)
        self.homeadd_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # Phone Number Label
        self.phonenum_label = ttk.Label(user_info_frame, text="Phone Number", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.phonenum_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Phone Number Entry
        self.phonenum_var = tk.StringVar()
        self.phonenum_entry = ttk.Entry(user_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.phonenum_var)
        self.phonenum_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # UserID Label
        self.userID_label = ttk.Label(account_info_frame, text="User ID", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.userID_label.pack(side="top",padx=20,pady=10, anchor='center')

        # UserID Entry
        self.userID_var = tk.StringVar()
        self.userID_entry = ttk.Entry(account_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.userID_var)
        self.userID_entry.pack(side="top",padx=20,pady=10, anchor='center')
        
        # Password Label
        self.password_label = ttk.Label(account_info_frame, text="Password", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.password_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Password Entry
        self.userpassword_var = tk.StringVar()
        self.password_entry = ttk.Entry(account_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", show="*", textvariable=self.userpassword_var)
        self.password_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # Initial Deposit Label
        self.initdep_label = ttk.Label(account_info_frame, text="Initial Deposit", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.initdep_label.pack(side="top",padx=20,pady=10, anchor='center')

        # Initial Deposit Entry
        self.initdep_var = tk.StringVar()
        self.initdep_entry = ttk.Entry(account_info_frame, font=("Berlin Sans FB Demi", 15, 'bold'), justify="center", textvariable=self.initdep_var)
        self.initdep_entry.pack(side="top",padx=20,pady=10, anchor='center')

        # Submit Label
        self.submit_label = ttk.Label(account_info_frame, text="Submit?", font=("Arial", 20, 'bold'), bootstyle='primary')
        self.submit_label.pack(side="top",padx=20,pady=10, anchor='center')

        button_frame = ttk.Frame(account_info_frame)
        button_frame.pack(side="top",padx=20,pady=10, anchor='center')

        # submit button
        self.submit = ttk.Button(
            button_frame,
            text="\u2713",
            bootstyle="success",
            command= lambda: self.submit_func(),
            width=8,
            )
        self.submit.pack(side="left",padx=5,pady=5,)

        # cancel button
        self.cancel = ttk.Button(
            button_frame,
            text="X",
            bootstyle="danger",
            command=lambda: self.cancel_function(),
            width=10,
            )
        self.cancel.pack(side="left", padx=10 ,pady=5, ipadx=10)

        self.mainloop()

    def center_window(self):
        window_width = self.size[0]
        window_height = self.size[1]
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")  

    def cancel_function(self):
        """Cancels the registration and destroys the window"""
        self.master.deiconify()
        self.destroy()
    
    def submit_func(self):
        """Checks if the entries are valid and submits the data to the database"""
        # Check if all entries are filled
        if self.surname_var.get() == "" or self.fstname_var.get() == "" or self.homeadd_var.get() == "" or self.phonenum_var.get() == "" or self.userID_var.get() == "" or self.userpassword_var.get() == "" or self.initdep_var.get() == "":
            msg.showerror("Invalid Input", "Please fill in all the entries.")
            return
        else:
            # Check if the userID is already taken
            if self.atm_db.view_user(self.userID_var.get()) != None:
                msg.showerror("Invalid Input", "User ID is already taken.")
                return
            else:
                # Create user
                self.atm_db.register_users(self.userID_var.get(), self.surname_var.get(), self.fstname_var.get(), self.homeadd_var.get(), self.phonenum_var.get())
                # Create account
                self.atm_db.register_account(self.userID_var.get(), self.userpassword_var.get(), self.initdep_var.get())
                # Show success message
                msg.showinfo("Success", "Account successfully created.")
                self.cancel_function()


class ATM_GUI(ttk.Toplevel):
    def __init__(self, title, size, acc_no):
        super().__init__(title=title, size=size)
        self.size = size
        self.center_window()
        self.atm_db = ATM_DB()
        self.acc_no = acc_no
        self.userID = self.atm_db.view_account(self.acc_no)[2]

        self.resizable(False, False)

        # Configure 2x2 grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.create_title_banner()
        self.info_frame = infoFrame(self)
        self.options_frame = OptionsFrame(self)

        self.mainloop()

    def center_window(self):
        window_width = self.size[0]
        window_height = self.size[1]
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")  

    def create_title_banner(self):
        """Creates the image banner at the top of the window"""
        # Image
        logo_frame = ttk.Frame(self)
        logo_image = tk.PhotoImage(file="Media/Lion_Icon.png")
        # Resize
        logo_image = logo_image.subsample(2,2)
        logo_label = ttk.Label(logo_frame, image=logo_image)
        logo_label.image = logo_image
        logo_label.pack(side="top", anchor='center')
        logo_frame.grid(row=0, column=0, sticky="ew")
        

        # Image
        title_frame = ttk.Frame(self)
        title_image = tk.PhotoImage(file="Media/Golden_Mane_Title.png")
        # Resize
        title_image = title_image.subsample(2,2)
        title_label = ttk.Label(title_frame, image=title_image)
        title_label.image = title_image
        title_label.pack(side="top", anchor='center')
        title_frame.grid(row=0, column=1, sticky="ew")


class infoFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=1, column=0, sticky="ew",)

        self.balance_var = tk.StringVar(value=f"\u20b1{self.master.atm_db.view_balance(self.master.acc_no)}")

        # Widgets
        self.create_welcome().pack(side="top",padx=20,pady=10, anchor='w')
        self.create_balance().pack(side="top",padx=20,pady=10, anchor='w')
        self.create_acc_type().pack(side="top",padx=20,pady=10, anchor='w')
        self.refresh_button = ttk.Button(self,text="Refresh", command=self.refresh).pack(side="top",padx=20,pady=10, anchor='w')

    def refresh(self):
        """Refreshes the balance label"""
        self.balance_var.set(f"\u20b1{self.master.atm_db.view_balance(self.master.acc_no)}")

    def create_welcome(self):
        welcome_frame = ttk.Frame(self)
        welcome_label = ttk.Label(welcome_frame, text="Welcome", font=("Arial", 15), bootstyle='primary')
        welcome_label.pack(side="top",anchor='w')

        self.user_var = tk.StringVar(value=self.master.atm_db.view_user(f'"{self.master.userID}"')[2])
        user_label = ttk.Label(welcome_frame, text=self.user_var.get(), font=("Berlin Sans FB Demi", 20, 'bold'))
        user_label.pack(side="top",anchor='w')

        return welcome_frame
    
    def create_balance(self):
        balance_frame = ttk.Frame(self)
        balance_labels = ttk.Label(balance_frame, text="Balance", font=("Arial", 15), bootstyle='primary') 
        balance_labels.pack(side="top",anchor='w')

        self.balance_label = ttk.Label(balance_frame, text=self.balance_var ,font=("Berlin Sans FB Demi", 20, 'bold'), textvariable=self.balance_var)
        self.balance_label.pack(side="top",anchor='w')

        return balance_frame
    
    def create_acc_type(self):
        acc_type_frame = ttk.Frame(self)
        acc_type_label = ttk.Label(acc_type_frame, text="Account Type", font=("Arial", 15), bootstyle='primary')
        acc_type_label.pack(side="top",anchor='w')

        acc_type_var = tk.StringVar(value=self.master.atm_db.view_account(self.master.acc_no)[1])
        acc_type_label = ttk.Label(acc_type_frame, text=acc_type_var.get(), font=("Berlin Sans FB Demi", 20, 'bold'))
        acc_type_label.pack(side="top",anchor='w')

        return acc_type_frame


class OptionsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=1, column=1, sticky="nsew", padx=20)

        # Configure a 2x2 grid
        self.frame = ttk.Frame(self,)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.pack(side="top", padx=10, pady=10, anchor='center', fill='x', expand=True)


        # Buttons - Deposit, Withdraw, View Transactions, Logout
        self.deposit_button = ttk.Button(
            self.frame, text="Deposit",
            bootstyle="primary",
            command= lambda: Deposit_Window(master=self.master),
            width=10,
            )
        self.deposit_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10,ipady=20)

        self.withdraw_button = ttk.Button(
            self.frame, text="Withdraw",
            bootstyle="primary",
            command=lambda : Withdraw_Window(master=self),
            width=10,
            )
        self.withdraw_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10,ipady=20)

        self.transactions_button = ttk.Button(
            self.frame, text="View Transactions",
            bootstyle="primary",
            command=lambda : Transactions_Window(master=self),
            width=10
            )
        self.transactions_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10,ipady=20)
        
        self.logout_button = ttk.Button(
            self.frame, text="Logout",
            bootstyle="danger",
            command= lambda: self.logout(),
            width=10
            )
        self.logout_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10,ipady=10)
    
    def logout(self):
        """Logs out the user destroys the window and deiconifies the login window"""
        self.master.master.deiconify()
        self.master.destroy()

class Deposit_Window(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Deposit")
        self.geometry("300x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # Title label
        self.label = ttk.Label(
            self,
            text="Enter Amount to Deposit",
            font=("Arial", 15, 'bold'),
            bootstyle='primary'
            )
        self.label.pack(side="top", padx=10, pady=10, anchor='center')

        # Create frame
        self.frame = ttk.Frame(self)
        self.frame.pack(side="top", padx=10, anchor='center', fill='both', expand=True)

        # Configure a 3x5 grid
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)

        # Create widgets
        self.create_widgets()

        # loop
        self.mainloop()
    
    def create_widgets(self):
        # entry widget and variable
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(
            self.frame,
            textvariable=self.entry_var,
            font=("Berlin Sans FB Demi", 15, 'bold'),
            justify="center"
            )
        self.entry.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10,ipady=10)

        # number buttons
        self.num_1 = ttk.Button(
            self.frame, text="1",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "1"),
            width=10,
            )
        self.num_1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_2 = ttk.Button(
            self.frame, text="2",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "2"),
            width=10,
            )
        self.num_2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_3 = ttk.Button(
            self.frame, text="3",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "3"),
            width=10,
            )
        self.num_3.grid(row=1, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_4 = ttk.Button(
            self.frame, text="4",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "4"),
            width=10,
            )
        self.num_4.grid(row=2, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_5 = ttk.Button(
            self.frame, text="5",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "5"),
            width=10,
            )
        self.num_5.grid(row=2, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_6 = ttk.Button(
            self.frame, text="6",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "6"),
            width=10,
            )
        self.num_6.grid(row=2, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_7 = ttk.Button(
            self.frame, text="7",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "7"),
            width=10,
            )
        self.num_7.grid(row=3, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_8 = ttk.Button(
            self.frame, text="8",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "8"),
            width=10,
            )
        self.num_8.grid(row=3, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_9 = ttk.Button(
            self.frame, text="9",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "9"),
            width=10,
            )
        self.num_9.grid(row=3, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_0 = ttk.Button(
            self.frame, text="0",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "0"),
            width=10,
            )
        self.num_0.grid(row=4, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        # submit button
        self.submit = ttk.Button(
            self.frame, text="\u2713",
            bootstyle="success",
            command= lambda: self.submit_func(self.master.acc_no, self.entry_var.get()),
            width=10,
            )
        self.submit.grid(row=4, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        # cancel button
        self.cancel = ttk.Button(
            self.frame, text="X",
            bootstyle="danger",
            command=lambda: self.destroy(),
            width=10,
            )
        self.cancel.grid(row=4, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

    def submit_func(self, account_number, amount):
        # Call the deposit method of the atm_db
        self.master.atm_db.deposit(account_number, amount)
        
        # Clear the entry widget
        self.entry_var.set("")

        # create an ok message box
        msg.showinfo("Deposit Successful", f"Your new balance is:\n\u20b1{self.master.atm_db.view_balance(account_number)}")


class Withdraw_Window(ttk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Withdraw")
        self.geometry("300x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # Title label
        self.label = ttk.Label(
            self,
            text="Enter Amount to Deposit",
            font=("Arial", 15, 'bold'),
            bootstyle='primary'
            )
        self.label.pack(side="top", padx=10, pady=10, anchor='center')

        # Create frame
        self.frame = ttk.Frame(self)
        self.frame.pack(side="top", padx=10, anchor='center', fill='both', expand=True)

        # Configure a 3x5 grid
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)

        # Create widgets
        self.create_widgets()

        # loop
        self.mainloop()
    
    def create_widgets(self):
        # entry widget and variable
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(
            self.frame,
            textvariable=self.entry_var,
            font=("Berlin Sans FB Demi", 15, 'bold'),
            justify="center"
            )
        self.entry.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10,ipady=10)

        # number buttons
        self.num_1 = ttk.Button(
            self.frame, text="1",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "1"),
            width=10,
            )
        self.num_1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_2 = ttk.Button(
            self.frame, text="2",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "2"),
            width=10,
            )
        self.num_2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_3 = ttk.Button(
            self.frame, text="3",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "3"),
            width=10,
            )
        self.num_3.grid(row=1, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_4 = ttk.Button(
            self.frame, text="4",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "4"),
            width=10,
            )
        self.num_4.grid(row=2, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_5 = ttk.Button(
            self.frame, text="5",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "5"),
            width=10,
            )
        self.num_5.grid(row=2, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_6 = ttk.Button(
            self.frame, text="6",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "6"),
            width=10,
            )
        self.num_6.grid(row=2, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_7 = ttk.Button(
            self.frame, text="7",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "7"),
            width=10,
            )
        self.num_7.grid(row=3, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_8 = ttk.Button(
            self.frame, text="8",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "8"),
            width=10,
            )
        self.num_8.grid(row=3, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_9 = ttk.Button(
            self.frame, text="9",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "9"),
            width=10,
            )
        self.num_9.grid(row=3, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

        self.num_0 = ttk.Button(
            self.frame, text="0",
            bootstyle="primary",
            command=lambda : self.entry_var.set(self.entry_var.get() + "0"),
            width=10,
            )
        self.num_0.grid(row=4, column=1, sticky="nsew", padx=10, pady=10,ipady=10)

        # submit button
        self.submit = ttk.Button(
            self.frame, text="\u2713",
            bootstyle="success",
            command= lambda: self.submit_func(self.master.acc_no, self.entry_var.get()),
            width=10,
            )
        self.submit.grid(row=4, column=0, sticky="nsew", padx=10, pady=10,ipady=10)

        # cancel button
        self.cancel = ttk.Button(
            self.frame, text="X",
            bootstyle="danger",
            command=lambda: self.destroy(),
            width=10,
            )
        self.cancel.grid(row=4, column=2, sticky="nsew", padx=10, pady=10,ipady=10)

    def submit_func(self, account_number, amount):
        # Call the deposit method of the atm_db
        status = self.master.atm_db.withdraw(account_number, int(amount))
        
        # Clear the entry widget
        self.entry_var.set("")

        # If status returns done, create an ok message box
        if type(status) == tuple:
            msg.showinfo("Withdrawal Successful", f"Your new balance is:\n\u20b1{self.master.atm_db.view_balance(account_number)}.\n{status[1]}")
        else:
            msg.showerror("Withdrawal Unsuccessful", status)


class Transactions_Window(ttk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("Transactions")
        self.geometry("500x400")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # Tkinter Table
        self.table = ttk.Treeview(self)
        self.table.pack(side="top", padx=10, pady=10, anchor='center', fill='both', expand=True)

        # define columns
        self.table['columns'] = ("Transaction Type", "Amount", "Date")

        # format columns
        self.table.column("#0", width=0, stretch="no")
        self.table.column("Transaction Type", anchor="center", width=150)
        self.table.column("Amount", anchor="center", width=150)
        self.table.column("Date", anchor="center", width=150)

        # create headings
        self.table.heading("#0", text="", anchor="w") 
        self.table.heading("Transaction Type", text="Transaction Type", anchor="center")
        self.table.heading("Amount", text="Amount", anchor="center")
        self.table.heading("Date", text="Date", anchor="center")

        # insert data
        id = 0
        for transaction in self.master.atm_db.view_all_transactions(self.master.acc_no):
            self.table.insert(parent='', index='end', iid=id, text="", values=(transaction[0], transaction[1], transaction[2]))
            id += 1

        self.mainloop()


if __name__ == "__main__":
    ATM_Login("Login to your account", (400, 480), "atm_theme")
