from difflib import SequenceMatcher

with open('sample.txt') as file_1, open('original.txt') as file_2:
    first_file = file_1.read()
    second_file = file_2.read()

    file_matched = SequenceMatcher(None, first_file, second_file).ratio()
    plagiarism_percentage = file_matched * 100
    print(f"The plagiarized content is {plagiarism_percentage:.2f}%")
import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

def calculate_plagiarism():
    file_1_path = file_1_entry.get()
    file_2_path = file_2_entry.get()

    try:
        with open(file_1_path, 'r') as file_1, open(file_2_path, 'r') as file_2:
            content_1 = file_1.read()
            content_2 = file_2.read()

            similarity_ratio = SequenceMatcher(None, content_1, content_2).ratio()
            plagiarism_percentage = similarity_ratio * 100

            result_label.config(text=f"The plagiarized content is {plagiarism_percentage:.2f}%")
    except FileNotFoundError:
        result_label.config(text="File not found. Please check the file paths.")

def browse_file(entry_widget):
    filename = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filename)

root = tk.Tk()
root.title("Plagiarism Checker")

# File 1 Entry
file_1_label = tk.Label(root, text="File 1:")
file_1_label.grid(row=0, column=0)
file_1_entry = tk.Entry(root, width=80)
file_1_entry.grid(row=0, column=1)
file_1_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_1_entry))
file_1_button.grid(row=0, column=2)

# File 2 Entry
file_2_label = tk.Label(root, text="File 2:")
file_2_label.grid(row=1, column=0)
file_2_entry = tk.Entry(root, width=80)
file_2_entry.grid(row=1, column=1)
file_2_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_2_entry))
file_2_button.grid(row=1, column=2)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Plagiarism", command=calculate_plagiarism)
calculate_button.grid(row=2, column=1)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1)

root.mainloop()
import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

def calculate_plagiarism():
    file_1_path = file_1_entry.get()
    file_2_path = file_2_entry.get()

    try:
        with open(file_1_path, 'r') as file_1, open(file_2_path, 'r') as file_2:
            content_1 = file_1.read()
            content_2 = file_2.read()

            similarity_ratio = SequenceMatcher(None, content_1, content_2).ratio()
            plagiarism_percentage = similarity_ratio * 100

            result_label.config(text=f"The similarity ratio is {plagiarism_percentage:.2f}%")
    except FileNotFoundError:
        result_label.config(text="File not found. Please check the file paths.")

def browse_file(entry_widget):
    filename = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filename)


root = tk.Tk()
root.title("Plagiarism Checker")

# File 1 Entry
file_1_label = tk.Label(root, text="File 1:")
file_1_label.grid(row=0, column=0)
file_1_entry = tk.Entry(root, width=70)
file_1_entry.grid(row=0, column=1, columnspan=2)
file_1_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_1_entry))
file_1_button.grid(row=0, column=3)

# File 2 Entry
file_2_label = tk.Label(root, text="File 2:")
file_2_label.grid(row=1, column=0)
file_2_entry = tk.Entry(root, width=70)
file_2_entry.grid(row=1, column=1, columnspan=2)
file_2_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_2_entry))
file_2_button.grid(row=1, column=3)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Similarity", command=calculate_plagiarism)
calculate_button.grid(row=2, column=2)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1, columnspan=2)

root.mainloop()
import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

def calculate_plagiarism():
    file_1_path = file_1_entry.get()
    file_2_path = file_2_entry.get()

    try:
        with open(file_1_path, 'r') as file_1, open(file_2_path, 'r') as file_2:
            content_1 = file_1.read()
            content_2 = file_2.read()

            similarity_ratio = SequenceMatcher(None, content_1, content_2).ratio()
            plagiarism_percentage = similarity_ratio * 100

            result_label.config(text=f"The similarity ratio is {plagiarism_percentage:.2f}%")
    except FileNotFoundError:
        result_label.config(text="File not found. Please check the file paths.")

def browse_file(entry_widget):
    filename = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filename)

root = tk.Tk()
root.title("Plagiarism Checker")

# File 1 Entry
file_1_label = tk.Label(root, text="File 1:")
file_1_label.grid(row=0, column=0, pady=5)
file_1_entry = tk.Entry(root, width=70)
file_1_entry.grid(row=0, column=1, columnspan=2)
file_1_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_1_entry))
file_1_button.grid(row=0, column=3)

# File 2 Entry
file_2_label = tk.Label(root, text="File 2:")
file_2_label.grid(row=1, column=0, pady=5)
file_2_entry = tk.Entry(root, width=70)
file_2_entry.grid(row=1, column=1, columnspan=2)
file_2_button = tk.Button(root, text="Browse", command=lambda: browse_file(file_2_entry))
file_2_button.grid(row=1, column=3)

# Calculate Buttton
calculate_button = tk.Button(root, text="Calculate Similarity", command=calculate_plagiarism)
calculate_button.grid(row=2, column=2, pady=10)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1, columnspan=2)


root.mainloop()
