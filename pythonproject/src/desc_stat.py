"""This is a script that will call the descriptive statistics function from lib.py"""
from src.lib import *

data = load_data_from_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv")

if data is not None:
    summary = summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")
