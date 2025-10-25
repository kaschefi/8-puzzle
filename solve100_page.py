import tracemalloc
from heuristic import *
from astar import *
import time
import threading
from tkinter import Frame, Label, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Solve100Page(Frame):
    """Page that solves 100 puzzles using Manhattan and Hamming heuristics."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#eaeaea")
        self.controller = controller

        # Title
        Label(
            self,
            text="Solve 100 Times Page",
            font=("Arial", 24, "bold"),
            bg="#eaeaea"
        ).pack(pady=50)


        Button(
            self,
            text="Run 100 Solves",
            font=("Arial", 14),
            bg="#b5e48c",
            relief="flat",
            width=20,
            height=2,
            command=self.solve_100_times
        ).pack(pady=20)

        self.result_label = Label(self, text="", font=("Arial", 14), bg="#eaeaea", justify="center")
        self.result_label.pack(pady=10)

        Button(
            self,
            text="Go Back",
            font=("Arial", 14),
            bg="#d9d9d9",
            relief="flat",
            width=20,
            height=2,
            command=lambda: controller.show_page("MainPage")
        ).pack(pady=20)


    def solve_100_times(self):
        """Start solving in a background thread to prevent UI freezing."""
        threading.Thread(target=self._run_solve_tests, daemon=True).start()

    def _run_solve_tests(self):
        #  in order to track memory usage,
        #  uncomment and delete three stars from the commented lines that start with # ***

        """Run the solve tests and display charts side by side in the center."""
        self.result_label.config(text="Running tests, please wait...")
        self.update_idletasks()

        # --- Run both solvers ---
        # ***add manhattan_mem as third return value
        manhattan_time, total_manhattan_nodes = self.solve100_heuristic(solve_with_manhattan)
        # ***add hamming_mem as third return value
        hamming_time, total_hamming_nodes= self.solve100_heuristic(solve_with_hamming)

        # Clear text status
        self.result_label.config(text="")
        summary = (
            f"Results after solving 100 puzzles:\n\n"
            f"Manhattan distance\n time: {manhattan_time:.2f}s, nodes: {total_manhattan_nodes}\n\n" #***, Memory usage: {manhattan_mem:.2f}MB\n\n"
            f"Hamming distance\n time: {hamming_time:.2f}s, nodes: {total_hamming_nodes}\n\n"#***, Memory usage: {hamming_mem:.2f}MB\n\n"
            f"{'Manhattan' if manhattan_time < hamming_time else 'Hamming'} "
            f"is faster by {abs(hamming_time - manhattan_time):.2f} seconds.\n"
            f"{'Manhattan' if total_manhattan_nodes < total_hamming_nodes else 'Hamming'} "
            f" have explored {abs(total_hamming_nodes - total_manhattan_nodes)} less nodes.\n"
            # ***f"{'Manhattan' if manhattan_mem < hamming_mem else 'Hamming'} "
            # ***f"have used {abs(hamming_mem - manhattan_mem):.2f} MB. less than {'Manhattan' if manhattan_mem > hamming_mem else 'Hamming'}"
        )
        self.result_label.config(text=summary)

    def solve100_heuristic(self, heuristic):
        total_nodes = 0
        start_time = (time.time())
        # ***tracemalloc.start()
        for _ in range(100):
            puzzle = generate_puzzle()
            path, node = heuristic(puzzle)
            total_nodes += node
        total_time = time.time() - start_time
        # ***current, peak = tracemalloc.get_traced_memory()
        # ***tracemalloc.stop()

        # Convert bytes to MB
        # ***peak_memory_mb = peak / (1024 * 1024)

        return total_time, total_nodes # ***, peak_memory_mb