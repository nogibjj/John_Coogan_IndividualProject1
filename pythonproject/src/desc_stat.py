import lib

data = lib.load_data_from_csv("pythonproject\src\data.csv")

if data is not None:
    summary = lib.summary_statistics(data)
    print(data.head())
    print(summary)
    print(" ")
