name = ""
running_total = 0.0
count = 0


def rainfalls():
    global name
    global count
    global running_total
    rainfall = open("rainfall-totals-1.txt")
    listing = rainfall.read()
    listing = listing.split()
    count = 1
    for name in listing:
        if count % 2 == 0:
            running_total = running_total + float(name)
        count = count + 1
    print("The Running total is: " + str(running_total) + " The average is: " + str(running_total / count))


try:
    rainfalls()
except IOError:
    print("File not found")
except ValueError:
    print("Invalid data: " + name + " Is not valid")
    print("The Running total is: " + str(running_total) + " The average is: " + str(running_total / count))
