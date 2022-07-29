import os

f = open("configuration.txt", "r")

searchPath = f.readline().split("\n")[0]
extension = f.readline().split("\n")[0]

f.close()

f = open("files.txt", "w")

for root, dirs, files in os.walk(searchPath):
    for file in files:
        if file.endswith(extension):
            f.write(os.path.join(root, file) + "\n")

f.close()
