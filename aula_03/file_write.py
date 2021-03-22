import os
from os import path

BASE_DIR = path.join(path.dirname(__file__), "files")
# names = ["joao", "maria", "pedro", "andre", "jose"]
# names = ["joao\n", "maria\n", "pedro\n", "andre\n", "jose\n"]
names = ("joao\n", "maria\n", "pedro\n", "andre\n", "jose\n")

# with open(path.join(BASE_DIR, "names.txt"), "w") as file:
#     for name in names:
#         file.write(name)
#         file.write("\n")

with open(path.join(BASE_DIR, "names.txt"), "w") as file:
    file.writelines(names)
