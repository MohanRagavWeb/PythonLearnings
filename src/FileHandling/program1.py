with open("sample.txt", "w") as f:
    f.write("Python File Handling\n")
    f.write("Line 2\n")

with open("sample.txt", "r") as f:
    print("Reading file:")
    print(f.read())

with open("sample.txt", "a") as f:
    f.write("New appended line\n")

with open("sample.txt", "r") as f:
    print("Final content:")
    print(f.read())
