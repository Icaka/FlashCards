import tkinter as tk
from tkinter import messagebox
# from interface.login_page import LoginPage
from user_controller import UserController
from user_registration import UserRegistration


class RegistrationPage(tk.Frame):
    def __init__(self, master, switch_view, u_controller: UserController, cards_controller):
        super().__init__(master)
        self.switch_view = switch_view
        self.u_controller = u_controller

        self.reg_label = tk.Label(self, text='Registration Page')
        self.reg_label.grid(row=0)

        self.fname_label = tk.Label(self, text='First Name')
        self.lname_label = tk.Label(self, text='Last Name')
        self.nick_label = tk.Label(self, text='Nickname')
        self.pass_label = tk.Label(self, text='Password')

        self.fname_entry = tk.Entry(self)
        self.lname_entry = tk.Entry(self)
        self.nick_entry = tk.Entry(self)
        self.pass_entry = tk.Entry(self)

        self.reg_button = tk.Button(self, text='Register', command=self.register)
        self.login_button = tk.Button(self, text='Back to Login', command=self.back_to_login)

        self.print_users_button = tk.Button(self, text='Print Users', command=self.print_users)

        self.set_layout()

    def set_layout(self):
        self.fname_label.grid(row=1, column=0)
        self.lname_label.grid(row=2, column=0)
        self.nick_label.grid(row=3, column=0)
        self.pass_label.grid(row=4, column=0)

        self.fname_entry.grid(row=1, column=1)
        self.lname_entry.grid(row=2, column=1)
        self.nick_entry.grid(row=3, column=1)
        self.pass_entry.grid(row=4, column=1)

        self.reg_button.grid(row=5, column=0)
        self.login_button.grid(row=5, column=1)

        self.print_users_button.grid(row=6, column=2)

    def register(self):
        messagebox.showinfo('reg_button', 'reg button pressed')
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        nick = self.nick_entry.get()
        password = self.pass_entry.get()
        new_user_reg = UserRegistration(fname, lname, nick, password)
        if self.u_controller.register(new_user_reg):
            messagebox.showinfo('Registration', 'Registration success')
            return True
        messagebox.showinfo('Registration', 'Registration failed')
        return False

    def back_to_login(self):
        from interface.login_page import LoginPage
        print('back lo login BUTTON PRESSED')
        # messagebox.showinfo('login_button', 'login button pressed')
        self.switch_view(LoginPage)
        pass

    def print_users(self):
        messagebox.showinfo('print_users', 'Printing all users to console')
        self.u_controller.print_all_users()
