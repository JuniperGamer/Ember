import os
import tkinter as tk
import webbrowser
import time
from PIL import Image, ImageTk, ImageFilter

def search_files(directory, query):
    matching_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if query in file:
                matching_files.append(os.path.join(root, file))
    
    return matching_files

def search_button_click():
    search_query = search_entry.get()
    results_text.config(state=tk.NORMAL)
    results_text.insert(tk.END, "Searching for file...\n")
    results_text.see(tk.END)  # Scroll to the end to show the message
    results_text.delete(1.0, tk.END)  # Clear previous results
    
    start_time = time.time()  # Record start time
    
    try:
        matching_files = search_files(os.path.expanduser("~"), search_query)
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        
        if matching_files:
            for file_path in matching_files:
                results_text.insert(tk.END, "Found: " + file_path + "\n")
        else:
            results_text.insert(tk.END, "No matching files found.")
    except Exception as e:
        results_text.insert(tk.END, "An error occurred: " + str(e))
    
    results_text.insert(tk.END, f"Search completed in {elapsed_time:.2f} seconds\n")
    results_text.config(state=tk.DISABLED)  # Prevent editing of results

def open_github():
    webbrowser.open("https://github.com/JuniperGamer/Ember")

# Create the main window
root = tk.Tk()
root.title("Ember File Search")

# Load and display the image on the button
logo_image = Image.open(r"C:\Users\brayd\OneDrive\Documents\Coding world\Other Languages\Python\Ember-removebg-preview.png")  # Replace with your logo's path
logo_image = logo_image.resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# GitHub button placement and text
follow_label = tk.Label(root, text="Follow the GitHub!")
follow_label.pack(side=tk.BOTTOM)
github_button = tk.Button(root, image=logo_photo, command=open_github)
github_button.pack(side=tk.BOTTOM)

# Create and place GUI elements
search_label = tk.Label(root, text="Enter file name:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack()

results_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
results_text.pack()

root.mainloop()
