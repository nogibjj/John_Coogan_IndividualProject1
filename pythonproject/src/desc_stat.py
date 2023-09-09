"""This is a script that will call the descriptive statistics function (describe()) from lib.py"""
import lib

data = lib.load_data_from_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv")

if data is not None:
    summary = lib.summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")
