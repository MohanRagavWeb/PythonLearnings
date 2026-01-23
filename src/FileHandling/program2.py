file_path = "../data.txt"

# Write to file
with open(file_path, "w") as f:
    f.write("Python File Handling Demo\n")
    f.write("This file is inside src folder\n")

print("File written successfully!")

# Read file
with open(file_path, "r") as f:
    print("\n--- Reading file ---")
    print(f.read())

# Append content
with open(file_path, "a") as f:
    f.write("New appended line\n")

print("\nContent appended successfully!")

# Read final content
with open(file_path, "r") as f:
    print("\n--- Final file content ---")
    print(f.read())
