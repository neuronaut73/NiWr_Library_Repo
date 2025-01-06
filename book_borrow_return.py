def borrow_return_book(df):
    """
    Updates the status of a book either from 0 (unborrowed) to 1 (borrowed)
    or in case of return from 1 (borrowed) to 0 (unborrowed).
    Requires the bookid as User Input

    Args:
        df (DataFrame): _description_

    Returns:
        df: The same dataframe only with updated status field.
    """
    while True:
        try:
            # Ask for the book ID
            bookid = int(input("Please enter the bookid: "))
            
            # Check if the bookid is valid
            if bookid in df["bookid"].values:
                # Get the current status of the book
                current_status = df.loc[df["bookid"] == bookid, "status"].iloc[0]
                
                if current_status == 0:
                    # If status is 0, book is available
                    df.loc[df["bookid"] == bookid, "status"] = 1
                    print(f"Book with bookid {bookid} is now borrowed. Please return it in two weeks.")
                else:
                    # If status is 1, book is already borrowed
                    df.loc[df["bookid"] == bookid, "status"] = 0
                    print(f"Book with bookid {bookid} has been returned. Thank you!")
                break  # Exit the loop after successful operation
            else:
                # Invalid bookid
                print("Invalid bookid. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the bookid.")
    return df