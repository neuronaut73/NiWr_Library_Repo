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

# Approach for 1 and 2: Using pandas DataFrame

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