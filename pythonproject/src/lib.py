"""importing pandas package for the describe function"""
import sys

sys.path.append("venv/lib/python3.11/site-packages")
# ignore lint errors for the following lines
import pandas as pd  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def plot_visualize(dataframe):
    auto_df = dataframe
    """A test of data visualization for a given data set"""
    weight = auto_df["weight"]
    mpg = auto_df["mpg"]

    fig, ax = plt.subplots()
    ax.scatter(weight, mpg)
    ax.set_xlabel("Vehicle Weight")
    ax.set_ylabel("MPG")
    ax.set_title("Scatter Plot of Vehicle Weight vs MPG by car origin")
    return fig


def save_plot(file_name, datafram):
    plot_visualize(datafram).savefig(
        "pythonproject/figures/" + f"scatter_plot_{file_name}.png"
    )


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
    summary = dataframe.describe()
    markdown_output = summary.to_markdown()
    return markdown_output


def df_min(dataframe, column_name):
    """Takes a dataframe and returns the minimum value of the dataframe
    Args:
        dataframe
    Returns:
        minimum value of the dataframe"""
    min = dataframe[column_name].min()
    return min


def df_max(dataframe, column_name):
    """Takes a dataframe and returns the maximum value of the dataframe
    Args:
        dataframe
    Returns:
        maximum value of the dataframe"""
    max = dataframe[column_name].max()
    return max
