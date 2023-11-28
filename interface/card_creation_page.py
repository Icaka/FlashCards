import tkinter as tk
from tkinter import messagebox
from flash_card_controller import FlashCardController


class CardCreationPage(tk.Frame):
    def __init__(self, master, switch_page, u_controller, c_controller: FlashCardController):
        super().__init__(master)
        self.switch_page = switch_page
        self.u_controller = u_controller
        self.card_controller = c_controller

        self.title_label = tk.Label(self, text='Card Creation Page')

        self.side1_entry = tk.Entry(self)
        self.side2_entry = tk.Entry(self)

        self.submit_button = tk.Button(self, text='Create!', command=self.create_card_button)
        self.back_button = tk.Button(self, text='Go Back', command=self.go_back)
        self.print_cards_button = tk.Button(self, text='Print Cards', command=self.print_cards)

        self.set_layout()

    def set_layout(self):
        self.title_label.grid(row=0, columnspan=2, pady=10)

        self.side1_entry.grid(row=1, column=0, padx=10, sticky=tk.W)
        self.side2_entry.grid(row=1, column=1, padx=10, sticky=tk.E)

        self.submit_button.grid(row=2, columnspan=2, pady=10)
        self.back_button.grid(row=3, columnspan=2)
        self.print_cards_button.grid(row=4, column=2, pady=20)

    def create_card_button(self):
        side_1 = self.side2_entry.get()
        side_2 = self.side2_entry.get()
        if self.card_controller.create_card(side_1, side_2):
            messagebox.showinfo('creation', 'Card created')
            return
        messagebox.showinfo('creation', 'Card creation failed')

    def go_back(self):
        from interface.home_page import HomePage
        self.switch_page(HomePage)

    def print_cards(self):
        self.card_controller.print_all_cards()

