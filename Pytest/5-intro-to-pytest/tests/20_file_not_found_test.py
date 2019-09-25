import pytest


def test_empty_file():
    with pytest.raises(FileNotFoundError):
        file = open("fileNotFound.txt")
        file.readline(1)
        with open("fileNotFound.txt") as file:
            for line in file:
                x = x + line
                print(line)

        file.write("Trying to insert this into the file")


def test_user_gives_file():
    fname = input("whats the file name?")
    fname += ".", input("what is the file type")

    with pytest.raises(FileNotFoundError):
        file = open(fname)
        file.readlines()


def test_open_test1_file():
    with open("test1.txt") as file:
        for line in file:
            print(line)


test_open_test1_file()
