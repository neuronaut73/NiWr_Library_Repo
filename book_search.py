def search_books(df):
    """
    This function allows to search for title or author name.
    The surch Function uses wild card.

    Args:
        df (DataFrame): The Library Data as Dataframe Format.

    Returns:
        filtered_df: Returns the filtered data frame,
    """
    choice_search = int(input("Search by title (1) or author (2)? Please enter 1 for title or 2 for author"))
    try:
        if choice_search == 1:
            title_search_term = input("Enter title search term")
            mask_title = df["title"].str.contains(title_search_term, case=False, na=False)
            filtered_df = df[mask_title]
        elif choice_search == 2:
            author_search_term = input("Enter author search term")
            mask_author = df["author"].str.contains(author_search_term, case=False, na=False)
            filtered_df = df[mask_author]
    except:
        print("Invalid choice - Please enter 1 for title or 2 for author")
    print(filtered_df)
    main_menu = input(print("Press m to return to the menu: "))
    if main_menu == "m":
        return 