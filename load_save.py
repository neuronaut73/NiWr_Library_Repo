import pandas as pd

def load_library(library_file_name):
    
    """ 
    Loads the Library Sample Data

    Args:
        library_file_name (str): This is the filename as specified in
        the library.py file (library.txt).
        

    Returns:
        DataFrame: The Library data as dataframe
    """

    
    try:
        df = pd.read_csv(library_file_name, delimiter="|")
    except:
        print("Error reading file. Please make sure library.txt is in the same directory as library.py")
    return df

def save_and_exit(library_file_name, df):
    try:
        with open(library_file_name, "w") as file:
            # Save the DataFrame to a file using the '|' delimiter
            df.to_csv(file, sep="|", index=False)
        print(f"Data successfully saved to {library_file_name}. Exiting program...")
        raise SystemExit(0)  
    except Exception as e:
        # Handle errors during file saving
        print(f"An error occurred while saving the file: {e}")
        raise SystemExit(1)  
