from tkinter import *

class Solve100Page(Frame):
    """Second page with a Back button."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#eaeaea")
        self.controller = controller

        Label(self, text="Solve 100 Times Page",
              font=("Arial", 24, "bold"), bg="#eaeaea").pack(pady=100)

        Button(self, text="Go Back",
               font=("Arial", 14), bg="#d9d9d9", relief="flat",
               width=20, height=2,
               command=lambda: controller.show_page("MainPage")).pack(pady=40)
