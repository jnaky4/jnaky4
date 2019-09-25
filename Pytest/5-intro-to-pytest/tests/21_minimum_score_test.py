import taco

# this test adds up an undefined amount of point deductions, but doesn't allow you to go beyond 0
# sorry ta's you can't give a negative grade
def test_subtract_score(*points):
    outof10 = 10
    for score in points:
        outof10 -= score
    assert outof10 >= 0
    return outof10


test_subtract_score(2, 3, 4)

"""
inp = 'a'
takeaway = 0
while(inp != 'q'):
    inp = input("enter a value, type q to quit")
    if inp != 'q':
        takeaway += int(inp)
        print(takeaway)

print("final point deducted: ", takeaway)
test_subtract_score(takeaway)
"""
file = open("test2.txt")
contents = file.read()
contents.strip(' ').split(',')
numcontents = [len(contents)]
taco.test()

contents = list(map(int, contents))
print(contents)
test_subtract_score(numcontents)

