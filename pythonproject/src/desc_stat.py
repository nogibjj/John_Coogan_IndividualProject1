"""This is a script that will call the descriptive statistics function from lib.py"""
import lib

data = lib.load_data_from_csv("https://www.statlearning.com/s/Auto.csv")

if data is not None:
    summary = lib.summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")
