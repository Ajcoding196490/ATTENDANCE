import sqlite3

# --- Configuration ---
DATABASE_FILE = "dragon.db"
TABLE_NAME = "CUSTOMER" # Replace with the actual name of your table

def read_table_fields(db_file, table_name):
    """
    Connects to the database and retrieves the column names (fields) for the specified table.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        print(f"--- 🐲 Analyzing Table Structure for '{table_name}' ---")
        
        # SQL Command to get table information (PRAGMA is an SQLite-specific command)
        # The result includes: (cid, name, type, notnull, dflt_value, pk)
        cursor.execute(f"PRAGMA table_info({table_name})")
        
        columns = [column[1] for column in cursor.fetchall()]
        
        if columns:
            print("✅ Fields (Columns) in the table:")
            for i, name in enumerate(columns):
                print(f"   {i+1}. {name}")
            return columns
        else:
            print(f"❌ Table '{table_name}' not found or has no columns.")
            return None

    except sqlite3.Error as e:
        print(f"❌ Database Error during field reading: {e}")
        return None
        
    finally:
        if conn:
            conn.close()

# ----------------------------------------------------------------------

def edit_table_data(db_file, table_name, column_to_edit, new_value, condition_column, condition_value):
    """
    Updates a specific column's value for rows matching a certain condition.
    
    WARNING: This example uses direct f-string formatting for the column name 
    and column to check, which is generally acceptable for *validated* column names. 
    However, for the *values*, we use a placeholder to prevent SQL Injection.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        print(f"\n--- ✏️ Editing Data in Table '{table_name}' ---")

        # The SQL UPDATE command
        # Syntax: UPDATE table SET column_to_change = new_value WHERE column_to_check = condition_value
        sql_command = f"""
        UPDATE {table_name} 
        SET {column_to_edit} = ?
        WHERE {condition_column} = ?;
        """
        
        # Execute the command with the values passed as a tuple to prevent SQL Injection
        cursor.execute(sql_command, (new_value, condition_value))
        
        # Commit the changes to the database
        conn.commit()
        
        rows_affected = cursor.rowcount
        
        if rows_affected > 0:
            print(f"✅ Success! {rows_affected} row(s) updated.")
            print(f"   Set '{column_to_edit}' to '{new_value}' where '{condition_column}' is '{condition_value}'.")
        else:
            print("⚠️ No rows were updated. Check your condition values.")

    except sqlite3.OperationalError as e:
        print(f"❌ SQL Error: {e}. Check if the table or column names are correct.")
    except sqlite3.Error as e:
        print(f"❌ Database Error during data editing: {e}")
        
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

# ----------------------------------------------------------------------

# --- Main Execution ---
if __name__ == "__main__":
    
    # 1. READ THE FIELDS (SCHEMA)
    # --------------------------
    fields = read_table_fields(DATABASE_FILE, TABLE_NAME)
    
    if fields:
        # Example of how to use the editing function based on the fields we just read.
        # This assumes your table has columns like 'name' and 'level'
        
        print("\n--- Example Data Edit (Manual Input Simulation) ---")
        
        # User/Script defines what to change
        COLUMN_TO_UPDATE = 'level'      # The column you want to change
        NEW_VALUE = 90                  # The new value you want to set
        CONDITION_COLUMN = 'name'       # The column used to find the specific row(s)
        CONDITION_VALUE = 'Charizard'   # The value in CONDITION_COLUMN to identify the row(s)
        
        print(f"Goal: Update '{COLUMN_TO_UPDATE}' to '{NEW_VALUE}' for the dragon named '{CONDITION_VALUE}'.")
        
        # 2. EDIT THE DATA (UPDATE)
        # --------------------------
        edit_table_data(
            db_file=DATABASE_FILE, 
            table_name=TABLE_NAME, 
            column_to_edit=COLUMN_TO_UPDATE, 
            new_value=NEW_VALUE, 
            condition_column=CONDITION_COLUMN, 
            condition_value=CONDITION_VALUE
        )