

def compare():
    list1 = account.read()
    list1 = list1.split(',')
    list2 = over_90.readlines()
    count = 0
    count_out = 0
    while count < len(list2):
        while count_out < len(list1):
            if list2[count].strip() == list1[count_out].strip():
                print(list1[count_out], end="")
                print(list1[count_out + 1], end="")
                print(list1[count_out + 2], end="")
                print(list1[count_out + 3], end="")
                print(list1[count_out + 4], end="")
            count_out = count_out + 1
        count = count + 1


try:
    account = open("accounts.txt", 'r')
    over_90 = open("over90.txt", 'r')
    print("The following accounts are overdue: ")
    compare()

    account.close()
    over_90.close()
except IOError:
    print("The File you are looking for was not found")
