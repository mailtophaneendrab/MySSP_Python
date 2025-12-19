# Read a file and count number of strings (words)

file_name = "../input.txt"

with open(file_name, "r", encoding="utf-8") as file:
    data = file.read()

words = data.split()
print("Count of strings:", len(words))