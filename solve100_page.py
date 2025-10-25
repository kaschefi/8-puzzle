from tkinter import *
import statistics
from heuristic import generate_puzzle, solve_with_manhattan, solve_with_hamming

class Solve100Page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#eaeaea")
        self.controller = controller

        Label(self, text="Solve 100 Times", font=("Arial", 24, "bold"),
              bg="#eaeaea").pack(pady=20)

        btn_frame = Frame(self, bg="#eaeaea")
        btn_frame.pack(pady=10)

        Button(btn_frame, text="Run 100 (Manhattan)", font=("Arial", 12),
               bg="#d9d9d9", relief="flat", width=20, height=2,
               command=lambda: self.run_series("manhattan")).grid(row=0, column=0, padx=10, pady=5)

        Button(btn_frame, text="Run 100 (Hamming)", font=("Arial", 12),
               bg="#d9d9d9", relief="flat", width=20, height=2,
               command=lambda: self.run_series("hamming")).grid(row=0, column=1, padx=10, pady=5)

        Button(btn_frame, text="Back", font=("Arial", 12),
               bg="#d9d9d9", relief="flat", width=20, height=2,
               command=lambda: controller.show_page("MainPage")).grid(row=0, column=2, padx=10, pady=5)

        self.status = Label(self, text="Ready.", font=("Arial", 12), bg="#eaeaea")
        self.status.pack(pady=15)

        self.results = Label(self, text="", font=("Consolas", 12), bg="#f7f7f7",
                             width=70, height=12, justify=LEFT, anchor=NW, relief="solid", bd=1)
        self.results.pack(pady=10)

        self.total_runs = 100

    def run_series(self, mode):
        import time
        self.mode = mode
        self.run_idx = 0
        self.times, self.nodes = [], []
        self.status.config(text=f"Running 100 {mode} tests...")
        self.results.config(text="")
        self.after(10, self._run_one)

    def _run_one(self):
        import time
        if self.run_idx >= self.total_runs:
            mean_t = statistics.mean(self.times)
            sd_t = statistics.stdev(self.times) if len(self.times) > 1 else 0
            mean_n = statistics.mean(self.nodes)
            sd_n = statistics.stdev(self.nodes) if len(self.nodes) > 1 else 0
            result = (f"Mode: {self.mode}\n"
                      f"Runs: {self.total_runs}\n"
                      f"Avg Time: {mean_t:.4f}s  ±{sd_t:.4f}\n"
                      f"Avg Nodes: {mean_n:.2f}  ±{sd_n:.2f}")
            self.results.config(text=result)
            self.status.config(text="Finished.")
            return

        puzzle = generate_puzzle()
        if self.mode == "manhattan":
            _, expanded, runtime = solve_with_manhattan(puzzle)
        else:
            _, expanded, runtime = solve_with_hamming(puzzle)

        self.times.append(runtime)
        self.nodes.append(expanded)
        self.run_idx += 1

        if self.run_idx % 10 == 0:
            self.status.config(text=f"Run {self.run_idx}/{self.total_runs}...")

        self.after(1, self._run_one)
