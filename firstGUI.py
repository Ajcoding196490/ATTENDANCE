import tkinter as tk
from tkinter import messagebox


# --- 1. Define the main function to handle the button click ---
def on_button_click():
    """
    Function to be called when the button is pressed.
    It reads the input, updates the output label, and clears the input box.
    """
    # Get the text currently in the input Entry widget
    user_input = input_box.get()

    if user_input:
        # Update the text of the output_label widget
        output_label.config(text=f"Hello, '{user_input}'!")
        
        # Clear the input box after reading the text
        input_box.delete(0, tk.END)
    else:
        # Show a simple dialog if the input box is empty
        messagebox.showwarning("Warning", "Please enter some text!")


# --- 2. Setup the main window (Root) ---
# Create the main window object
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x200") # Set the initial size of the window (Width x Height)

# --- 3. Create Widgets (The visual elements) ---

# A. Text Input (Entry)
# We use a Label to tell the user what to do
input_label = tk.Label(root, text="Enter your name:")
input_label.pack(pady=5) # 'pack' is a simple layout manager

# The actual text box where the user types
input_box = tk.Entry(root, width=40)
input_box.pack(pady=5)
input_box.focus() # Automatically set the cursor to the input box

# B. Button
# The command=on_button_click links the button press to the function defined above
action_button = tk.Button(root, text="Click Me!", command=on_button_click)
action_button.pack(pady=10)

# C. Output (Label)
# This label starts empty and will be updated by the button function
output_label = tk.Label(root, text="Output will appear here...", fg="blue")
output_label.pack(pady=5)


# --- 4. Run the main loop ---
# This starts the GUI event loop, which listens for clicks, key presses, etc.
root.mainloop()

# Note: The 'root.mainloop()' call must be the last line executed in the script.