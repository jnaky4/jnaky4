import pytest
import main


def test_login():
    username = main.get_username()
    password = main.get_password()
    assert username == 'Jacob Alongi' and password == '1234'


def test_login_fail():
    username = main.get_username()
    password = main.get_password()
    assert username == 'Caleb' and password == '69withTacos!!!'

# base on grade score of 10


def test_subtract_score():
    assert main.subtract_score(2, 3, 4) >= 0


def test_subtract_score_fail():
    assert main.subtract_score(5, 5, 5) >= 0


def test_empty_file():
    with pytest.raises(FileNotFoundError):
        file = open(main.input_empty_file())
        file.readline(1)

        with open(main.input_empty_file()) as file:
            for line in file:
                x = x + line
                print(line)
        file.write("trying to insert this into the file")


def test_empty_file_fail():
    with pytest.raises(FileNotFoundError):
        file = open("test1.txt")
        with open(file) as file:
            for line in file:
                x = x + line
                print(line)


def test_open_test1_file():
    file = main.open_test1_file("test1.txt")
    print(file)
    assert file == "username: Jacob Alongi"


def test_open_test1_file_fail():
    file = main.open_test1_file("test1.txt")
    print(file)
    assert file == "username: Caleb Kalimari"


def test_set_grade():
    assert 'B' == main.set_grade(80)


def test_set_grade_fail():
    assert 'A' == main.set_grade(-69)


