files = ["data1.csv", "data2.csv", "data3.csv"]

for file in files:
    if file.endswith(".csv"):
        print(file, "is a valid data file")
    else:
        print("Invalid file")
