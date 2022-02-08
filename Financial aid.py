bool_student = False
bool_GPA = False
bool_Drugs = False
bool_CrHr = False
bool_income = False
temp_str = input("Are you a new or returning student? Please enter y or n :")
if temp_str == "y":
    bool_student = True
if temp_str == "n":
    bool_student = False
temp_float = input("What is your GPA?:")
temp_float = float(temp_float)
if temp_float >= 2.0:
    bool_GPA = True
if temp_float < 2.0:
    bool_GPA = False
temp_str = input("Have you been convicted of a drug felony? Please enter y or n:")
if temp_str == "y":
    bool_Drugs = False
if temp_str == "n":
    bool_Drugs = True
temp_float = input("How many credit hours are you taking?:")
temp_float = float(temp_float)
if temp_float >= 6:
    bool_CrHr = True
if temp_float < 6:
    bool_CrHr = False
temp_float = input("What is your yearly gross income?:")
temp_float = float(temp_float)
if temp_float <= 50000:
    bool_income = True
if temp_float > 50000:
    bool_income = False
if bool_income and bool_CrHr and bool_GPA and bool_Drugs and bool_student:
    print("You are eligible to apply for financial aid")
else:
    print("You are not eligible to apply for financial aid")
