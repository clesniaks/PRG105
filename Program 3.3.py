cost = 0
discount = 0.0
print("Play prices per ticket:\n")
print(" 1.Student $5.00 \n 2.Veteran $7.00 \n 3.Show Sponsor $2.00 \n 4.Retiree $6.00 \n 5.General Public $10.00")
selection = input("Please enter the number of the category you fit for purchasing tickets:")
selection = int(selection)
num_tickets = input("Please enter the number of tickets you wish to purchase:" + "\n")
num_tickets = int(num_tickets)
if selection == 1:
    cost = 5*num_tickets
elif selection == 2:
    cost = 7*num_tickets
elif selection == 3:
    cost = 2*num_tickets
elif selection == 4:
    cost = 6*num_tickets
elif selection == 5:
    cost = 10*num_tickets
else:
    print("That is not a number between 1-5!")
if 4 < num_tickets < 8:
    discount = 0.1
elif 9 < num_tickets < 15:
    discount = 0.15
elif num_tickets > 15:
    discount = 0.20
else:
    discount = 0

print("Cost before any discounts were applied: $" + str(format(cost, '.2f')))
print("Your price after all discounts were applied is: $" + str(format(cost*(1-discount), '.2f')))
print("Your price is " + str(format((cost*(1-discount))/num_tickets, '.2f')) + " per ticket")
