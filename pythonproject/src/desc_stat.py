"""This is a script that will call the descriptive statistics function from lib.py"""
import lib


def main():
    """Main function to call data visualization functions"""
    data = lib.load_data_from_csv("https://www.statlearning.com/s/Auto.csv")

    if data is not None:
        summary = lib.summary_statistics(data)

    print(summary)

    lib.plot_visualize(data)
    lib.save_plot("ScatterPlot", data)

    # print(lib.df_min(data,"weight"))
    # print(lib.df_max(data,"cylinders"))


if __name__ == "__main__":
    main()
