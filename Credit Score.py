str_Credit = ""
credit_score = input("What is your credit score?:")
credit_score = int(credit_score)
if credit_score < 629:
    str_Credit = "Bad"
elif credit_score < 689:
    str_Credit = "Fair"
elif credit_score < 719:
    str_Credit = "Good"
else:
    str_Credit = "Excellent"
credit_score = str(credit_score)
print("With a credit score of " + credit_score + ":")
print("You have " + str_Credit + " credit")
