# with open("data.txt", "r") as file:
#     print(file.read())
# lines = ["Python\n", "Data Engineering\n", "ETL\n"]
#
# with open("output.txt", "w") as file:
#     file.writelines(lines)

# file = open("data.txt", "r")
#
# print(file.tell())  # pointer position
# file.seek(0)        # move pointer to start
# print(file.read())
#
# print(file.tell())
# file.close()

# import os
#
# if os.path.exists("GIT COMMANDS.txt"):
#     print("File exists")
# else:
#     print("File doesn't exist")



# file = open("newfile.txt","w")
# file.write("Hello World")


# import csv
#
# rows = [
#     ["Name", "Age"],
#     ["Mohan", 21],
#     ["Vijay",22]
# ]
#
# with open("output.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# import csv
#
# with open("output.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import json
#
# data = {"name": "Mohan", "role": "DE Intern","age":23}
#
# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)
