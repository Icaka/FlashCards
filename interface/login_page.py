import tkinter as tk
from tkinter import messagebox
from user_controller import UserController
from interface.registration_page import RegistrationPage


class LoginPage(tk.Frame):
    def __init__(self, master, switch_view, u_controller, card_controller):
        super().__init__(master)
        self.switch_view = switch_view
        self.u_controller: UserController = u_controller
        self.card_controller = card_controller
        # master.title("Login")

        self.login_label = tk.Label(self, text="Login Page")
        self.login_label.grid(row=0)

        self.nickname_label = tk.Label(self, text='Nickname').grid(row=1)
        self.pass_label = tk.Label(self, text='Password').grid(row=2)
        self.en1 = tk.Entry(self)
        self.en1.grid(row=1, column=1)
        self.en2 = tk.Entry(self)
        self.en2.grid(row=2, column=1)

        self.login_button = tk.Button(self, text="Log in", command=self.login)
        self.login_button.grid(row=3)

        self.reg_button = tk.Button(self, text='Register', command=lambda: self.switch_view(RegistrationPage))
        self.reg_button.grid(row=4)

    def login(self):
        text1 = self.en1.get()
        text2 = self.en2.get()
        if self.u_controller.login(text1, text2):
            messagebox.showinfo("Login", f"button clicked {text1} {text2}, login successful")
            from interface.home_page import HomePage
            self.switch_view(HomePage)
        else:
            messagebox.showinfo("Login", f"button clicked {text1} {text2}, login fail")
        pass
