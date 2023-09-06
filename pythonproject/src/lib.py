import pandas as pd


def load_data_from_csv(file_path):
    """Load the desired CSV data file for descriptive statistics
    takes a str file path to the CSV file
    returns a pd.DataFrame"""

    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


def summary_statistics(dataframe):
    """Takes the DataFrame and calls the describe function on it
    Args:
        DataFrame
    Returns:
        DataFrame containing summary statistics"""

    return dataframe.describe()
