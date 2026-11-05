# age
# is_employed(boolean)
# credit_score(integer)
# annual_income(float)
# has_collateral(boolean)

age = int(input("how old are you? --> "))
is_employed = bool(input("are you employed? (True or False) --> "))
credit_score = int(input("what is your credit score? --> "))
annual_income = float(input("how much is your annual income? --> "))
has_collateral = bool(input("do you have a collateral? (True or False) --> "))

# calculation

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("YOU ARE VALID")
    print("================")
    if credit_score >= 750: #tier 1
        print("you have a good credit score!")
        if annual_income >= 100000:
            base_rate = 4.5
            print("you have a good salary and good credit score, your interest is now", base_rate)
            print("=====================================================================")
        else:
            base_rate = 5.0
            print("you have a good salary and good credit score, your interest is now", base_rate)
    elif credit_score == 600 and credit_score <= 750:
            print("you have a good credit score")
            if has_collateral == True:
                 base_rate = 7.0
            elif annual_income <= 40000:
                base_rate = 9.5
            else:
                base_rate = 8.0
    else:
        print("INVALID!")
else:
    print("REJECTED: INVALID INFORMATION SUBMITTED")