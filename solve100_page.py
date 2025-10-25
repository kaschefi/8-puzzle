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

        # Run button
        btn_frame = Frame(self, bg="#eaeaea")
        btn_frame.pack(pady=40)
        Button(
            btn_frame,
            text="Run 100 Solves",
            font=("Arial", 14),
            bg="#b5e48c",
            relief="flat",
            width=20,
            height=2,
            command=self.solve_100_times
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            text="Go Back",
            font=("Arial", 14),
            bg="#d9d9d9",
            relief="flat",
            width=20,
            height=2,
            command=lambda: controller.show_page("MainPage")
        ).grid(row=0, column=1, padx=10)

        self.result_label = Label(self, text="", font=("Arial", 14), bg="#eaeaea", justify="center")
        self.result_label.pack(pady=10)

        # Chart area (empty until results appear)
        self.chart_frame = Frame(self, bg="#eaeaea")
        self.chart_frame.pack(pady=10)
        # Back button


    def solve_100_times(self):
        """Start solving in a background thread to prevent UI freezing."""
        threading.Thread(target=self._run_solve_tests, daemon=True).start()

    def _run_solve_tests(self):
        """Run the solve tests and display charts side by side in the center."""
        self.result_label.config(text="Running tests, please wait...")
        self.update_idletasks()

        # --- Run both solvers ---
        manhattan_time, total_manhattan_nodes ,manhattan_mem= self.solve100(solve_with_manhattan)
        hamming_time, total_hamming_nodes, hamming_mem= self.solve100(solve_with_hamming)

        # Clear text status
        self.result_label.config(text="")

        # --- Clear any old charts from the chart frame ---
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # --- Data setup ---
        heuristics = ['Manhattan', 'Hamming']

        # --- Chart 1: Total Time ---
        fig1, ax1 = plt.subplots(figsize=(3.2, 2.2))
        times = [manhattan_time, hamming_time]
        ax1.bar(heuristics, times, color=['#52b788', '#fb8500'])
        ax1.set_title("Total Time (s)", fontsize=10)
        ax1.set_ylabel("Seconds", fontsize=9)
        ax1.tick_params(axis='both', labelsize=9)
        fig1.tight_layout(pad=2)

        canvas1 = FigureCanvasTkAgg(fig1, master=self.chart_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", padx=10, pady=5, anchor="center")

        # --- Chart 2: Total Nodes ---
        fig2, ax2 = plt.subplots(figsize=(3.2, 2.2))
        nodes = [total_manhattan_nodes, total_hamming_nodes]
        ax2.bar(heuristics, nodes, color=['#74c69d', '#ffb703'])
        ax2.set_title("Nodes Explored", fontsize=10)
        ax2.set_ylabel("Count", fontsize=9)
        ax2.tick_params(axis='both', labelsize=9)
        fig2.tight_layout(pad=2)

        canvas2 = FigureCanvasTkAgg(fig2, master=self.chart_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", padx=10, pady=5, anchor="center")

        summary = (
            f"Manhattan time: {manhattan_time:.2f}s, nodes: {total_manhattan_nodes} Mem:{manhattan_mem:.2f}MB\n"
            f"Hamming time: {hamming_time:.2f}s, nodes: {total_hamming_nodes} Mem:{hamming_mem:.2f}MB"
        )
        self.result_label.config(text=summary)

    def solve100(self, heuristic):
        total_nodes = 0
        start_time = (time.time())
        tracemalloc.start()
        for _ in range(100):
            puzzle = generate_puzzle()
            path, node = heuristic(puzzle)
            total_nodes += node
        total_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Convert bytes to MB
        peak_memory_mb = peak / (1024 * 1024)

        return total_time, total_nodes, peak_memory_mb