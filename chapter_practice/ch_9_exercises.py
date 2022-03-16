import pickle
"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 9.1 Dictionaries
print("=" * 10, "Section 9.1 dictionaries", "=" * 10)
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14', 'Chase': 'September 30', 'Jimmy': 'July 26', 'Tom': 'May 4'}

# 2) Print Meri's Birthday
print(birthdays['Kathy'])
# 3) Create an empty dictionary named registration
registration = {}
# You will use the following dictionary for many of the remaining exercises"
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# 1) Print the keys and the values of miles_ridden using a for loop


def print_keys():
    for key in miles_ridden:
        print(key + " ", end='')
        print(miles_ridden[key])


print_keys()
# 2) Get the value for June 3 and print it, if not found display 'Entry not found', replace the ""


def june3_search():
    if miles_ridden.get('June 3', 0) != 0:
        value = miles_ridden['June 3']
        print(value)
    else:
        print("Entry not found")


june3_search()
# 3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the ""


def june6_search():
    if miles_ridden.get('June 6', 0) != 0:
        value2 = miles_ridden['June 6']
        print(value2)
    else:
        print("Entry not found")


june6_search()
# 4) Use the values method to print the miles_ridden dictionary


def value_search():
    values_in = miles_ridden.values()
    for key in values_in:
        print(key)


value_search()
# 5) Use the keys method to print all of the keys in miles_ridden


def key_search():
    keys_in = miles_ridden.keys()
    for key in keys_in:
        print(key)


key_search()
# 6) Use the pop method to remove June 4 then print the contents of the dictionary


def pop_it():
    miles_ridden.pop('June 4')
    print(miles_ridden)


pop_it()
# 7) Use the items method to print the contents of the miles_ridden dictionary


def items():
    print(miles_ridden.items())


items()
# TODO 9.2 Sets
print("=" * 10, "Section 9.2 sets", "=" * 10)
# 1) Create an empty set named my_set
my_set = set()
# 2) Create a set named days that contains the days of the week
days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# 3) Get the number of elements from the days set and print it
print(len(days))
# 4) Remove Saturday and Sunday from the days set
days.remove('Saturday')
days.remove('Sunday')

# 5) Determine if 'Mon' is in the days set
if 'Mon' not in days:
    print("Mon is not in days")
else:
    print("Mon is in days")

# TODO 9.3 Serializing Objects (Pickling)
print("=" * 10, "Section 9.3 serializing objects using the pickle library", "=" * 10)
# 1) Import the pickle library at the top of this file

# 2) Create the output file log and open it for binary writing
outfile = open('BinaryWrite.dat',  'wb')
# 3) Pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, outfile)
# 4) Close the log file
outfile.close()
