import tkinter as tk
from tkinter import messagebox

# --- Constants ---
# Define colors for a simple, modern look
BG_COLOR = "#f0f0f5"
FIELD_BG = "#ffffff"
ACCENT_COLOR = "#4CAF50" # Green
TEXT_COLOR = "#333333"

def submit_feedback():
    """
    Retrieves input data, prints it to the console, and clears the fields.
    """
    # Get data from entry fields (Name, Email)
    name = name_entry.get()
    email = email_entry.get()

    # Get data from the Text widget (Feedback). 
    # "1.0" means line 1, character 0 (start of the text). 
    # "end-1c" means the very end of the text, minus one character (to exclude the trailing newline).
    feedback = feedback_text.get("1.0", "end-1c").strip()
    
    # Simple validation check
    if not name or not email or not feedback:
        # Instead of using alert(), we use tkinter's messagebox
        messagebox.showerror("Submission Error", "Please fill out all fields before submitting.")
        return

    # Print the collected feedback data to the console (as requested)
    print("-" * 30)
    print("NEW CUSTOMER FEEDBACK SUBMITTED:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback:\n{feedback}")
    print("-" * 30)

    # Clear the input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    
    # Clear the Text widget
    feedback_text.delete("1.0", tk.END)

    # Optionally give the user visual confirmation in the GUI
    messagebox.showinfo("Success", "Thank a you! Your feedback has been submitted.")


# --- Main Application Setup ---

# Initialize the main window
root = tk.Tk()
root.title("Customer Feedback")
root.config(bg=BG_COLOR)

# --- Title Header ---
title_label = tk.Label(
    root, 
    text="Please provide feedback on your experience",
    font=("Inter", 16, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    pady=15
)
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

# --- Name Input ---
name_label = tk.Label(root, text="Name:", font=("Inter", 11), bg=BG_COLOR, fg=TEXT_COLOR)
name_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="w")

name_entry = tk.Entry(root, width=40, font=("Inter", 11), bg=FIELD_BG, fg=TEXT_COLOR, bd=1, relief="solid")
name_entry.grid(row=1, column=1, padx=(5, 20), pady=5, sticky="ew")

# --- Email Input ---
email_label = tk.Label(root, text="Email:", font=("Inter", 11), bg=BG_COLOR, fg=TEXT_COLOR)
email_label.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="w")

email_entry = tk.Entry(root, width=40, font=("Inter", 11), bg=FIELD_BG, fg=TEXT_COLOR, bd=1, relief="solid")
email_entry.grid(row=2, column=1, padx=(5, 20), pady=5, sticky="ew")

# --- Feedback Label ---
# Now placed in column 0 of row 3
feedback_label = tk.Label(root, text="Feedback:", font=("Inter", 11), bg=BG_COLOR, fg=TEXT_COLOR)
# Use sticky="nw" to align it to the top-left of the cell, next to the Text widget
feedback_label.grid(row=3, column=0, padx=(20, 5), pady=(15, 5), sticky="nw")

# --- Feedback Text Box ---
# Now placed in column 1 of row 3
feedback_text = tk.Text(
    root, 
    width=50, 
    height=10, 
    font=("Inter", 10), 
    bg=FIELD_BG, 
    fg=TEXT_COLOR, 
    bd=1, 
    relief="solid", 
    padx=5, 
    pady=5
)
feedback_text.grid(row=3, column=1, padx=(5, 20), pady=(15, 5), sticky="nsew")

# Configure rows and columns to resize gracefully
root.grid_columnconfigure(1, weight=1)
# The row containing the feedback box is now row 3
root.grid_rowconfigure(3, weight=1) 

# --- Submit Button ---
submit_button = tk.Button(
    root, 
    text="Submit", 
    command=submit_feedback,
    font=("Inter", 12, "bold"),
    bg=ACCENT_COLOR,
    fg="white",
    activebackground="#388E3C",
    activeforeground="white",
    cursor="hand2",
    relief="raised",
    padx=10,
    pady=5
)
# Moved to the next available row (row 4)
submit_button.grid(row=4, column=0, columnspan=2, padx=20, pady=(15, 20), sticky="s")


# --- Main Loop ---
if __name__ == "__main__":
    root.mainloop()