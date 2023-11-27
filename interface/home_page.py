import tkinter as tk
from tkinter import messagebox
from user_controller import UserController


class HomePage(tk.Frame):
    def __init__(self, master, switch_page, u_controller: UserController):
        super().__init__(master)
        self.switch_page = switch_page
        self.u_controller = u_controller

        self.greeting_label = tk.Label(self, text=f'hello {u_controller.currently_logged_user.user_name}')

        self.logout_button = tk.Button(self, text='Logout', command=self.logout)

        self.greeting_label.grid(row=0)
        self.logout_button.grid(row=1)

    def logout(self):
        self.u_controller.logout()
        messagebox.showinfo('logout', 'Logging out')
        from interface.login_page import LoginPage
        self.switch_page(LoginPage)
