import os
from os import path

BASE_DIR = path.join(path.dirname(__file__), "files")
file = open(path.join(BASE_DIR, "names.txt"))

data = file.read()
print(data)

data = file.readline()
print(data)

data = file.readlines()
print(data)
