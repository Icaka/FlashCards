import tkinter as tk
from tkinter import messagebox
from user_controller import UserController
from flash_card_controller import FlashCardController


class HomePage(tk.Frame):
    def __init__(self, master, switch_page, u_controller: UserController, card_controller: FlashCardController):
        super().__init__(master)
        self.switch_page = switch_page
        self.u_controller = u_controller
        self.card_controller = card_controller

        self.greeting_label = tk.Label(self, text=f'hello {u_controller.currently_logged_user.user_name}')

        self.logout_button = tk.Button(self, text='Logout', command=self.logout)
        self.card_create_button = tk.Button(self, text='Create Card', command=self.card_create)

        self.greeting_label.grid(row=0)
        self.logout_button.grid(row=1, pady=10)
        self.card_create_button.grid(row=2, pady=10)

        self.quiz_button = tk.Button(self, text='Quiz Time!', command=self.enter_quiz_page)
        self.quiz_button.grid(row=3, pady=10)

    def logout(self):
        self.u_controller.logout()
        messagebox.showinfo('logout', 'Logging out')
        from interface.login_page import LoginPage
        self.switch_page(LoginPage)

    def card_create(self):
        from interface.card_creation_page import CardCreationPage
        self.switch_page(CardCreationPage)

    def enter_quiz_page(self):
        from interface.quiz_page import QuizPage
        self.switch_page(QuizPage)
