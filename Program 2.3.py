income = input("What is your monthly income?:")
income = float(income)
EXP_housing = input("What is your monthly expenses on Housing?:")
EXP_housing = float(EXP_housing)
EXP_food = input("What is your monthly expenses on Food?:")
EXP_food = float(EXP_food)
EXP_Trans = input("What is your monthly expenses on Transportation?:")
EXP_Trans = float(EXP_Trans)
EXP_phone = input("What is your monthly Phone bill?:")
EXP_phone = float(EXP_phone)
EXP_util = input("What is your monthly expenses on Utilities?:")
EXP_util = float(EXP_util)
EXP_cloth = input("What is your monthly expenses on clothes?:\n")
EXP_cloth = float(EXP_cloth)
print("Housing takes up " + format((EXP_housing/income), '.2%') + " of your monthly budget")
print("Food takes up " + format((EXP_food/income), '.2%') + " of your monthly budget")
print("Transportation takes up " + format((EXP_Trans/income), '.2%') + " of your monthly budget")
print("Your Phone bill takes up " + format((EXP_phone/income), '.2%') + " of your monthly budget")
print("Utilities take up " + format((EXP_util/income), '.2%') + " of your monthly budget")
print("Clothing takes up " + format((EXP_cloth/income), '.2%') + " of your monthly budget")
print("You have " + str(income-(EXP_cloth+EXP_util+EXP_phone+EXP_Trans+EXP_housing+EXP_food)) + " left after expenses")
