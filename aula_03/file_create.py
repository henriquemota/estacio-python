import os
from os import path

BASE_DIR = path.join(path.dirname(__file__), "files")
file = open(path.join(BASE_DIR, "file.txt"), "a")
