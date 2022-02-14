savings_contribution = 0
counter = 0
age = input("What is your current age?:")
retirement_age = input("What age do you plan on retiring?:")
income = input("What is your yearly income?:")
percent_savings = input("What percent of your income do you save?:")
savings = input("How much money do you have in savings?:")
savings = float(savings) * 1.06
savings += (float(percent_savings)/100 * float(income))
savings_contribution = float(income) * float(percent_savings)/100
int(counter)
print("This projection assumes a 3% raise each year and a 6% yearly return on investment.")
print("Year      " + "Income   " + "Savings Contribution    " + "Total Savings")
for counter in range(1, (int(retirement_age)-int(age))+1):
    print(format(counter, '4.0f') + format(float(income), '14.0f') + format(float(savings_contribution), '14.0f') + str(format(float(savings), '14.0f')))
    counter = counter + 1
    income = float(income) * 1.03
    savings_contribution = float(income) * float(percent_savings)/100
    savings = float(savings) * 1.06
    savings += savings_contribution
