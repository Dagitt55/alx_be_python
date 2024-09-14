# finance_calculator.py

def calculate_savings(income, expenses):
    """
    Calculate monthly savings by subtracting expenses from income.
    """
    return income - expenses

def project_annual_savings(monthly_savings, interest_rate):
    """
    Project annual savings including interest.
    """
    annual_savings = monthly_savings * 12
    return annual_savings + (annual_savings * interest_rate)

def main():
    """
    Main function to interact with the user and perform calculations.
    """
    try:
        # User Input
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your total monthly expenses: "))
        
        # Calculate Monthly Savings
        monthly_savings = calculate_savings(monthly_income, monthly_expenses)
        
        # Project Annual Savings
        interest_rate = 0.05
        projected_annual_savings = project_annual_savings(monthly_savings, interest_rate)
        
        # Output Results
        print(f"Your monthly savings: ${monthly_savings:.2f}")
        print(f"Projected annual savings including interest: ${projected_annual_savings:.2f}")

    except ValueError:
        print("Please enter valid numerical values for income and expenses.")

if __name__ == "__main__":
    main()
