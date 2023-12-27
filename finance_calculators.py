def calculate_simple_interest(principal, rate, time):
    interest = principal * (1 + (rate / 100) * time)
    return interest

def calculate_compound_interest(principal, rate, time):
    interest = principal * (1 + rate / 100) ** time
    return interest

def calculate_bond_repayment_value(present_value, interest_rate, months):
    monthly_interest_rate = interest_rate / 100 / 12
    repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** -months)
    return repayment

# Get user input for the type of calculation for either investment or bond repayment.
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == 'investment':
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years the money will be invested: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == 'simple':
        result = calculate_simple_interest(amount, interest_rate, years)
    elif interest_type == 'compound':
        result = calculate_compound_interest(amount, interest_rate, years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        result = None

    if result is not None:
        print(f"The total amount after {years} years will be: {result}")

elif choice == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate per annum (as a percentage): "))
    months = int(input("Enter the number of months to repay the bond: "))

    repayment = calculate_bond_repayment_value(present_value, interest_rate, months)
    print(f"The monthly bond repayment will be: {repayment:.2f}")

else:
    print("Invalid choice. Please enter 'investment' or 'bond'.")
