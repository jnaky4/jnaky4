def get_username():
    username = 'Jacob Alongi'
    return username


def get_password():
    password = '1234'
    return password


def subtract_score(*points):
    out_of_10 = 10
    for score in points:
        out_of_10 -= score
    return out_of_10


def input_empty_file():
    file = "fileNotFound.txt"
    return file


def open_test1_file(file):
    x = ''
    with open("test1.txt") as file:
        for line in file:
            x += line
            print(line)
    return x


def set_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade < 90 and grade >= 80:
        return 'B'
    elif grade < 80 and grade >= 70:
        return 'C'
    elif grade < 70 and grade >= 60:
        return 'D'
    else:
        return 'F'

