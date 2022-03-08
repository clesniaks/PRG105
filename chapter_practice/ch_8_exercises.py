"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
length = len(name)
count = 0
while count < length:
    print(name[count])
    count = count + 1
# 2) Use the index value to access and print the capital s in Schmidt from the variable name
print('\n' + name[24])
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
print('\n')
count = -7
while count < 0:
    print(name[count])
    count = count + 1
# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle = name[5:10]
print(middle)
# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result


def teststrJacob():
    is_jacob = False
    if 'Jacob' in name:
        is_jacob = True
    else:
        is_jacob = False
    print(is_jacob)


teststrJacob()
# 2) Test to see if the string "Michael" is in name, print the result


def teststr():
    is_michael = False
    if 'Michael' in name:
        is_michael = True
    else:
        is_michael = False
    print(is_michael)


teststr()
# 3) Test to see if name contains a number, print the result


def testnum():
    is_int = False
    if name.isdigit():
        is_int = True
    else:
        is_int = False
    print(is_int)


testnum()
# 4) Test to see if number contains a number, print the result


def num():
    number = "42"
    has_int = False
    if number.isdigit():
        has_int = True
    else:
        has_int = False
    print(has_int)


num()
# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print


def replace():
    global name
    name = name.replace('J', 'j')
    print(name)


replace()
# 6) Split the string name into the variable name_list, replace the "", print the result


def split():
    global name
    name_list = name.split()
    print(name_list)


split()
