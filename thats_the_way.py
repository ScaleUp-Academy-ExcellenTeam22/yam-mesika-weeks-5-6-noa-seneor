import os
_path = input("enter your directory path")
if os.path.isdir(_path):
    print(list(filter(lambda x: x.startswith("deep"), os.listdir(_path))))
else:
    print("not a directory")
