import sqlite3
import re
import os

# --- Configuration ---
# CHANGED TO YOUR SPECIFIED DATABASE FILE NAME
DATABASE_FILE = "dragon.db" 

def get_valid_table_name():
    """Prompts the user for a table name and validates it."""
    while True:
        table_name = input(f"Enter the name for your new table: ")
        
        # Simple validation: checks if the name is not empty and contains only alphanumeric characters and underscores
        if not table_name:
            print("❌ Table name cannot be empty. Please try again.")
        # SQLite best practice: start with a letter and only use letters, numbers, and underscores.
        elif not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", table_name):
            print("⚠️ Table names should start with a letter or underscore and contain only letters, numbers, and underscores. Please try again.")
        else:
            return table_name

def create_table(db_file, table_name):
    """
    Connects to the SQLite database and creates a new table with the specified name.
    """
    conn = None
    try:
        # Connect to the database file ("dragon.db" in this case)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        print(f"\nAttempting to connect to '{db_file}'...")
        
        # Define the SQL command to create the table
        sql_command = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            level INTEGER
        );
        """
        
        # Execute the SQL command
        cursor.execute(sql_command)
        
        # Commit the changes to the database
        conn.commit()
        
        print(f"✅ Success! Table '{table_name}' has been created (or already exists) in '{db_file}'.")

    except sqlite3.Error as e:
        print(f"❌ An error occurred: {e}")
        
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("Database connection closed.")


# --- Main Execution ---
if __name__ == "__main__":
    
    # 1. Get a validated table name from the user
    new_table_name = get_valid_table_name()
    
    # 2. Execute the table creation function
    create_table(DATABASE_FILE, new_table_name)
    
    # Optional: List files to show the database file was created
    if os.path.exists(DATABASE_FILE):
        print(f"\nDatabase file location: {os.path.abspath(DATABASE_FILE)}")