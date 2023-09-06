import lib

data = lib.load_data_from_csv('')

if data is not None:
    summary = lib.summary_statistics(data)
    print(summary)