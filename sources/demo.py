# this small snippet of code intends to demonstrate the use of the linter
import os


def main():
    # first, some code that must be ok with the linter
    # test if the ressources exists in the ressources/raw_data folder
    if os.path.exists("ressources/raw_data"):
        print("The path exists")
        # then print the content of the folder
        print(os.listdir("ressources/raw_data"))
    else:
        print("The path does not exist")

    # then, some code that must be flagged by the linter
    a = 0
    b = 1
    print(a+b)
