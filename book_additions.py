import pandas as pd

def add_book(df):
    """
    Add a new record to the dataframe

    Args:
        df (DataFrame): The input dataframe (the library data)

    Returns:
        df: The updated dataframe with the new book addition
    """
    title = input("Enter title: ")
    author = input("Enter author: ")
    while True:
        try:
            year = int(input("Enter publication year (0-2025): "))
            if 0 <= year <= 2025:
                break
            print("Invalid year. Please enter a number between 0 and 2025.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print("New book additions have always status=0 which means available and not in borrowed state")
    status = 0
    bookid = df["bookid"].max()+1
    new_row = pd.DataFrame([{"bookid": bookid, "title": title, "author": author, "year": year, "status": status}])
    df = pd.concat([df, new_row], ignore_index=True)
    print("Success. I added this record to the library:")
    print(df.tail(1).to_string(index=False))  # Prints the last row of the DataFrame
    return df