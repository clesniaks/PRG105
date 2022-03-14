
def phrasing():
    phrase = input("Please enter a phrase to convert:")
    listing = phrase.split()
    count = 0
    while count < len(listing):
        print(listing[count][0].upper(), end="")
        count = count + 1


phrasing()
