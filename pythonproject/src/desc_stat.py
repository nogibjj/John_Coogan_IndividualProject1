"""This is a script that will call the descriptive statistics function from lib.py"""
from pythonproject.src.lib import load_data_from_csv
from pythonproject.src.lib import summary_statistics

data = load_data_from_csv("https://www.statlearning.com/s/Auto.csv")

if data is not None:
    summary = summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")
