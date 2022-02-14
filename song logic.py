num = 1
beer = 99
while num in range(1, 100):
    if beer == 1:
        print(str(beer) + " bottle of beer on the wall,")
        print(str(beer) + " bottle of beer")
        print("Take one down, pass it around")
    else:
        print(str(beer) + " bottles of beer on the wall,")
        print(str(beer) + " bottles of beer")
        print("Take one down, pass it around")
    beer = beer - 1
    if beer == 1:
        print(str(beer) + " bottle of beer on the wall\n")
    else:
        print(str(beer) + " bottles of beer on the wall\n")
    num = num + 1
