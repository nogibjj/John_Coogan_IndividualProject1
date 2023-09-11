"""This is a script that will call the descriptive statistics function from lib.py"""
from pythonproject.src.lib import load_data_from_csv
from pythonproject.src.lib import summary_statistics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = load_data_from_csv("https://www.statlearning.com/s/Auto.csv")

if data is not None:
    summary = summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")


def plot_visualize(dataframe):
    """A test of data visualization for a given data set"""
    origin_categories = ["American", "European", "Japanese"]
    data["origin"] = pd.Categorical(data["origin"], origin_categories)
    sns.lmplot(x="weight", y="mpg", data=data, hue="Origin")
    plt.xlabel("Vehicle Weight")
    plt.ylabel("MPG")
    plt.title("Scatter Plot of Vehicle Weight vs MPG by car origin")
    plt.show()
    return None


def main():
    """Main function to call data visualization functions"""
    plot_visualize(data)


if __name__ == "__main__":
    main()
