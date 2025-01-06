# Please see Readme File for Problem Structuring and Solution Description

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