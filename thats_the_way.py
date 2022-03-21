import os


def files_deep():
    """
    asks the user a directory path
    :return: list of all files in the directory that starts with deep
    """
    _path = input("enter your directory path: ")
    if os.path.isdir(_path):
        return [x for x in os.listdir(_path) if x.startswith("deep")]
    else:
        return "not a directory"


print(files_deep())
