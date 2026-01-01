import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("feedback_data.csv")

# Main Window
root = tk.Tk()
root.title("College Event Feedback Analysis")
root.geometry("500x400")
root.config(bg="#f4f6f7")

# Title
tk.Label(
    root,
    text="College Event Feedback Analysis",
    font=("Arial", 16, "bold"),
    bg="#f4f6f7"
).pack(pady=10)

# Functions
def show_summary():
    avg_rating = data["Event_Rating"].mean()
    recommend_percent = (data["Would_Recommend"].value_counts(normalize=True) * 100)

    summary = (
        f"Average Event Rating: {avg_rating:.2f}\n\n"
        f"Recommendation Percentage:\n"
        f"Yes: {recommend_percent.get('Yes', 0):.1f}%\n"
        f"No: {recommend_percent.get('No', 0):.1f}%"
    )

    messagebox.showinfo("Feedback Summary", summary)

def plot_ratings():
    data["Event_Rating"].value_counts().sort_index().plot(
        kind="bar",
        title="Event Rating Distribution"
    )
    plt.xlabel("Rating")
    plt.ylabel("Number of Students")
    plt.show()

def plot_satisfaction():
    data["Overall_Satisfaction"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Overall Satisfaction"
    )
    plt.ylabel("")
    plt.show()

# Buttons
tk.Button(root, text="Show Feedback Summary", width=25, command=show_summary).pack(pady=10)
tk.Button(root, text="Show Rating Chart", width=25, command=plot_ratings).pack(pady=10)
tk.Button(root, text="Show Satisfaction Chart", width=25, command=plot_satisfaction).pack(pady=10)
tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=20)

root.mainloop()
