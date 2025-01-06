# Requirements:
# 1. The program should allow users to:
#     - Add new books (title, author, publication year) -> need to append books
#     - List all books in the library               
#     - Search for books by title or author             -> searchable by title or author
#     - Mark books as borrowed or returned              -> add flag key if borrowed or not
#     - Save the library data to a file when exiting    -> write to file
#     - Load the library data from a file when starting -> read from file (write dummy data)

# 2. Each book should store:
#     - Title
#     - Author
#     - Publication year
#     - Status (borrowed or available)
# -> 4 keys: title, author, publication year, status

# Approach for 1 and 2: Nested Dictionary

# 3. The program should have a menu-driven interface with these options:
# === Library Manager ===
# 1. Add Book
# 2. List All Books
# 3. Search Books
# 4. Borrow/Return Book
# 5. Save and Exit
# Print simple menu and wait for choice (1-5)

# 4. The program should save data to a file called "library.txt" so books persist between program runs -> name of the file is library.txt

# 5. **Error Handling Requirements:** -> use try-except in main function
# - Handle invalid year inputs when adding books                -> except invalid year
# - Handle invalid menu selections                              -> except invalid menu selections (must be 1-5)
# - Handle file reading/writing errors                          -> except file reading/writing errors -> use with open
# - Handle invalid book selections when borrowing/returning     -> except book not found or already borrowed or already returned

import os
import pandas as pd
from book_additions import add_book
from book_search import search_books
from load_save import load_library, save_and_exit
from book_borrow_return import borrow_return_book
 
LIBRARY_FILE_NAME = "library.txt"  

def list_all_books(df):
    print(df)
    return


menu_text = """
=== Library Manager ===
1. Add Book
2. List All Books
3. Search Books
4. Borrow/Return Book
5. Save and Exit
"""

menu_options = {
    1: add_book,
    2: list_all_books,
    3: search_books,
    4: borrow_return_book,
    5: save_and_exit
}

def main():
    df = load_library(LIBRARY_FILE_NAME)
    while True:
        print(menu_text)
        try:
            choice = int(input("Enter choice from 1 to 5: "))
            action = menu_options.get(choice)
            if choice == 1:
                df = action(df)
            elif 2 <= choice <= 4:
                action(df)
            elif choice == 5:
                action(LIBRARY_FILE_NAME,df)
            else: 
                print("Invalid menu selection (must be an integer from 1 to 5)")
        except SystemExit:
            # Allow SystemExit to terminate the program gracefully
            raise
        except Exception as e:
            print(f"An Error occurred: {e}")
            
if __name__ == "__main__":
    main()