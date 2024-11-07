import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class DatavisApp:
    def __init__(self, master):
        self.master = master
        master.title("Datavis App")
        master.geometry("800x600")

        # Create a container for the plots
        self.plot_container = tk.Frame(master)
        self.plot_container.pack(fill=tk.BOTH, expand=True)

        # Create buttons to switch between plots
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.scatter_button = tk.Button(self.button_frame, text="Scatter Plot", command=self.plot_scatter)
        self.scatter_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.heatmap_button = tk.Button(self.button_frame, text="Heatmap", command=self.plot_heatmap)
        self.heatmap_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Initialize the scatter plot
        self.plot_scatter()

    def plot_scatter(self):
        # Clear the plot container
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        month = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]
        attendance = np.random.randint(50, 1000, 7)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(month, attendance)
        ax.set_xticks(np.arange(len(month)), labels=month)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        ax.set_title("Attendance")

        canvas = FigureCanvasTkAgg(fig, master=self.plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self.plot_container)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_heatmap(self):
        # Clear the plot container
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        month = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]
        schools = ["Jacobs Younguns", "Mafia Kidz.", "Lil Sheetos", "Soap droppers", "Mangetout's Mangled", "Stink gang", "Kidz."]
        attendance = np.random.randint(50, 1000, [7, 7])

        fig, ax = plt.subplots(figsize=(8, 6))
        im = ax.imshow(attendance)

        ax.set_xticks(np.arange(len(month)), labels=month)
        ax.set_yticks(np.arange(len(schools)), labels=schools)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        for i in range(len(month)):
            for j in range(len(schools)):
                text = ax.text(j, i, attendance[i, j], ha="center", va="center", color="w")

        ax.set_title("Attendance Heatmap")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self.plot_container)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
app = DatavisApp(root)
root.mainloop()