import os


def get_path():
    os.chdir("..")
    path = os.getcwd() + "/resources/input.txt"
    return path
