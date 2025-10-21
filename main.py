from tkinter import *
from manhattan import *   # your puzzle logic file
from solve100_page import Solve100Page
delay = 300

class PuzzleUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("8 Puzzle Solver")
        self.configure(bg="#eaeaea")
        self.geometry("800x600")
        self.resizable(False, False)

        # Main container for all pages
        self.container = Frame(self, bg="#eaeaea")
        self.container.pack(fill="both", expand=True)

        # Register all pages here
        self.pages = {}
        for Page in (MainPage, Solve100Page):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show main page initially
        self.show_page("MainPage")

    def show_page(self, page_name):
        """Raise a specific page to the front."""
        frame = self.pages[page_name]
        frame.tkraise()


class MainPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#eaeaea")
        self.controller = controller

        # Title
        Label(self, text="welcome to 8 puzzle solver",
              font=("Arial", 24, "bold"), bg="#eaeaea").pack(pady=30)

        # Puzzle frame
        self.puzzle_frame = Frame(self, bg="#eaeaea")
        self.puzzle_frame.pack(pady=10)

        # Load initial puzzle
        self.puzzle = generate_puzzle()
        self.tiles = []
        self.draw_puzzle()

        # Button frame
        btn_frame = Frame(self, bg="#eaeaea")
        btn_frame.pack(pady=40)

        Button(btn_frame, text="solve with manhattan distance",
               font=("Arial", 12), bg="#d9d9d9", relief="flat",
               width=25, height=2, command=self.solve_manhattan).grid(row=0, column=0, padx=10)

        #  Switch to Solve100Page when clicked
        Button(btn_frame, text="solve for 100 times",
               font=("Arial", 12), bg="#d9d9d9", relief="flat",
               width=25, height=2,
               command=lambda: controller.show_page("Solve100Page")).grid(row=0, column=1, padx=10)

        Button(btn_frame, text="solve with hamming distance",
               font=("Arial", 12), bg="#d9d9d9", relief="flat",
               width=25, height=2, command=self.solve_hamming).grid(row=0, column=2, padx=10)

        Button(btn_frame, text="regenerate puzzle",
               font=("Arial", 12), bg="#d9d9d9", relief="flat",
               width=25, height=2, command=self.regenerate_puzzle).grid(row=1, column=1, padx=10, pady=10)

    def draw_puzzle(self):
        """Draws the 3x3 grid based on self.puzzle."""
        for r in range(3):
            for c in range(3):
                val = self.puzzle[r][c]
                color = "white" if val == 0 else "#42b8ff"
                label = Label(self.puzzle_frame, text=str(val) if val != 0 else "",
                              font=("Arial", 28, "bold"),
                              bg=color, fg="black", width=4, height=2, borderwidth=2, relief="solid")
                label.grid(row=r, column=c, padx=2, pady=2)
                self.tiles.append(label)

    def update_puzzle_ui(self):
        """Updates puzzle labels with current puzzle state."""
        for r in range(3):
            for c in range(3):
                val = self.puzzle[r][c]
                label = self.tiles[r * 3 + c]
                label.config(text=str(val) if val != 0 else "",
                             bg="white" if val == 0 else "#42b8ff")

    def solve_manhattan(self):
        print("Solving with Manhattan distance...")
        path = solve_with_manhattan(self.puzzle)
        step_index = 0

        def show_next_step():
            nonlocal step_index
            if step_index >= len(path):
                print("Animation finished.")
                return

            self.puzzle = path[step_index]
            self.update_puzzle_ui()
            step_index += 1
            self.after(delay, show_next_step)

        show_next_step()

    def solve_hamming(self):
        print("Solving with Hamming distance...")

    def regenerate_puzzle(self):
        print("Regenerating puzzle...")
        self.puzzle = generate_puzzle()
        self.update_puzzle_ui()


if __name__ == "__main__":
    app = PuzzleUI()
    app.mainloop()
