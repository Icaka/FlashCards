import tkinter as tk
from tkinter import messagebox
from user_controller import UserController
from flash_card_controller import FlashCardController
from quiz_controller import QuizController


class QuizPage(tk.Frame):
    def __init__(self, master, switch_page, u_controller: UserController, c_controller: FlashCardController):
        super().__init__(master)
        self.switch_page = switch_page
        self.u_controller = u_controller
        self.card_controller = c_controller
        self.quiz_controller = QuizController(self.card_controller.flash_repo, self.u_controller.get_currently_logged_user())

        self.title_label = tk.Label(self, text='Quiz Page')
        self.title_label.grid(row=0, columnspan=2, pady=10)

        self.start_button = tk.Button(self, text='Start Quiz', command=self.start)
        self.start_button.grid(row=1, column=0, columnspan=1, pady=10)

        self.back_button = tk.Button(self, text='Go Back', command=self.go_back)
        self.back_button.grid(row=1, column=1, columnspan=1, padx=10)


    def start(self):
        self.quiz_frame = tk.Frame(self)
        self.quiz_frame.grid(row=2, columnspan=2)
        self.good_guesses = 0
        # entry_var = tk.StringVar(self.quiz_frame, 'text var')
        self.card_label = tk.Label(self.quiz_frame, text='text')
        self.card_label.grid(row=0, column=0)
        self.guess_entry = tk.Entry(self.quiz_frame)
        self.guess_entry.grid(row=0, column=1)

        self.guess_button = tk.Button(self.quiz_frame, text='Guess', command=self.check_guess)
        self.guess_button.grid(row=1, columnspan=2)
        self.quiz_controller.create_set_first_20()
        self.current_quiz = self.quiz_controller.get_quiz_set()
        self.current_card = None
        # print('HERE')
        self.next_card()
        """
        for question in self.quiz_controller.get_quiz_set():
            # label_text.question.side1
            card_label['text'] = question.side1
            guess_button.wait_variable(entry_var)
            messagebox.showinfo('question', f'side1: {question.side1}, side2: {question.side2}')
            if self.u_controller.get_currently_logged_user().guess_flash_card(question, entry_var):
                print('Correct')
            else:
                print('False')
            print(entry_var)
        self.quiz_frame.grid_forget()
        """

    def next_card(self):
        if self.current_quiz:
            self.current_card = self.current_quiz.pop(0)
            print(f'current card: {self.current_card.side1}')
            self.card_label.config(text=f'{self.current_card.side1}')
            self.guess_entry.delete(0, tk.END)
            messagebox.showinfo('question', f'side1: {self.current_card.side1}, side2: {self.current_card.side2}')
        else:
            print("Quiz over")
            messagebox.showinfo('quiz end', f'good guesses: {self.good_guesses}')
            self.good_guesses = 0
            self.quiz_frame.destroy()

    def check_guess(self):
        guess = self.guess_entry.get().strip()

        user_guess_res: bool = self.u_controller.currently_logged_user.guess_flash_card(self.current_card, guess)  # so that the user saves info about the current card

        # if guess == self.current_card.side2:
        if user_guess_res:
            print('Correct')
            self.good_guesses += 1
        else:
            print('False')
        self.next_card()

    def go_back(self):
        from interface.home_page import HomePage
        self.switch_page(HomePage)