import tkinter as tk
from tkinter import ttk

class HelloTranslatorApp(tk.Tk):
    """
    A simple "Hello" translator application built with Tkinter using a class structure.
    The main button cycles through different language greetings and updates a single output label.
    """
    def __init__(self):
        # Initialize the main window (parent class)
        super().__init__()

        self.title("The 'Hello' Translator")
        self.geometry("450x450")
        self.config(padx=20, pady=20)

        # Configure the grid layout to center content
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # List of greetings to cycle through (Greeting, Language Name)
        self.greetings = [
            ("¡Hola!", "Español"),
            ("Bonjour!", "Français"),
            ("Hallo!", "Nederlands"),
            ("Hello!", "English"),
            ("Guten Tag!", "Deutsch") # Added one more for fun
        ]
        self.language_index = 0 # Tracks which greeting is currently displayed

        self.create_widgets()

    def translate_hello(self):
        """
        Action commanded by the button. Cycles through the list of greetings
        and updates the output label text.
        """
        # Get the current greeting and language name using the index
        greeting, language = self.greetings[self.language_index]

        # Update the output label
        new_text = f"The greeting is: {greeting} (in {language})"
        self.output_label.config(text=new_text, fg="#0056b3") # Update color for visual feedback

        # Move to the next index, wrapping around to 0 if we hit the end
        self.language_index = (self.language_index + 1) % len(self.greetings)

    def create_widgets(self):
        """
        Sets up and places all GUI components (widgets) in the window.
        """
        
        # 1. Initial Instruction Label (Row 0)
        self.initial_label = ttk.Label(
            self,
            text="Welcome. Click the button to cycle through greetings.",
            font=("Inter", 12, "bold"),
            foreground="#333333"
        )
        self.initial_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")


        # --- 2. Input/Language Section (Rows 1-4) ---
        languages = [("Español", "Spanish"), ("Français", "French"), ("Nederlands", "Dutch"), ("English", "English")]
        
        # Create 4 Text Boxes in a Column (Rows 1-4)
        for i, (native_name, english_name) in enumerate(languages):
            # Text Box (Entry)
            entry = ttk.Entry(self, width=25)
            # Insert the native language name directly into the text box
            entry.insert(0, native_name)
            entry.config(state='readonly') # Set to read-only 
            # Place the entry, spanning both columns (columnspan=2)
            entry.grid(row=i + 1, column=0, columnspan=2, sticky="ew", pady=5)


        # The static 'Hola' label has been removed entirely (no Row 5 element for it).


        # --- 3. Action Button (Row 5 - Moved up) ---
        self.action_button = ttk.Button(
            self,
            text="Translate 'Hello'",
            command=self.translate_hello, # Link the button to the method
            cursor="hand2"
        )
        # The button is now placed directly after the language text boxes (Row 5)
        self.action_button.grid(row=5, column=0, columnspan=2, pady=(20, 10), sticky="ew")


        # --- 4. Final Output Label (Row 6 - Moved up) ---
        # This is where the translation answer will appear, immediately below the button.
        self.output_label = ttk.Label(
            self,
            text="Click the button above to start!",
            font=("Inter", 13, "bold"),
            foreground="#0056b3"
        )
        self.output_label.grid(row=6, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    # Create the instance of the application class
    app = HelloTranslatorApp()
    
    # Start the main event loop
    app.mainloop()