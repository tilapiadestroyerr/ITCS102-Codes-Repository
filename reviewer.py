#inputs 
age = int(input("age --> "))
monthly_revenue = float(input("your monthly revenue --> "))
cc = int(input("your credit score --> "))
years_in_business = float(input("years in business --> "))
has_defaults = bool(input("file for bankruptcy --> "))
collateral_name = str(input("collateral name --> "))
collateral_value = float(input("value of collateral --> "))

#eligibility check
max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("eligibility passed")
    if cc >= 720: #tier1
        print("high credit score!")
        max_loan = 3 * monthly_revenue
        if monthly_revenue >= 50000:
            print("monthly revenue is good")
            base_fee = max_loan * 0.015
        else:
            print("below 50000")
            base_fee * max_loan * 0.025
    elif cc >= 620 and cc < 720:
        print("credit score is within the range of 620 and  720")
        max_loan = 1.5 * monthly_revenue
        print("maximum loan --> ",max_loan)
        if years_in_business >= 5:
            print("business is more than 5 years")
            base_fee = max_loan * 0.02
            print("base fee rate is",base_fee)
        else:
            print("business is less than 5 years")
            base_fee = max_loan * 0.02
            print("base fee rate is",base_fee)
    elif cc <= 620 and cc > 1:
        print()
else:
    print("rejected:high risk or ineligible owner") 