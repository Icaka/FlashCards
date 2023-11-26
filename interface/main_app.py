import tkinter as tk
from tkinter import messagebox
from user_controller import UserController
from interface.login_page import LoginPage

WIN_WIDTH = 400
WIN_HEIGHT = 400


class MainApp(tk.Tk):  # extends tk.Tk class
    def __init__(self, user_c: UserController):
        super().__init__()
        self.u_controller = user_c
        self.title("Flash Cards App")
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.menu_frame: tk.Frame() = None
        self.current_view_frame: tk.Frame = None
        self.startup()

    def startup(self):
        self.menu_frame = tk.Frame(self, width=WIN_WIDTH, height=75, background="skyblue2")
        self.menu_frame.pack()
        self.minsize(400, 400)
        self.maxsize(400, 400)
        self.switch_view(LoginPage)

    def switch_view(self, frame_class: tk.Frame):
        new_view = frame_class(self, self.switch_view, self.u_controller)  # also passing the switch_view function
        if self.current_view_frame:
            self.current_view_frame.destroy()
        self.current_view_frame = new_view
        self.current_view_frame.pack()
