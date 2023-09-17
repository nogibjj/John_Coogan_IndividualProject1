"""This is a script that will call the descriptive statistics function from lib.py"""
import lib
import matplotlib.pyplot as plt


data = load_data_from_csv("https://www.statlearning.com/s/Auto.csv")

if data is not None:
    summary = summary_statistics(data)
    print(summary)


def plot_visualize(dataframe):
    auto_df = dataframe
    """A test of data visualization for a given data set"""
    weight = auto_df["weight"]
    mpg = auto_df["mpg"]

    plt.scatter(weight, mpg)
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
