# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print("Current Date and Time:", formatted_date)

def calculate_future_date(days):
    """Calculate and display the future date based on user input."""
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future Date after adding {days} days:", formatted_future_date)

def main():
    display_current_datetime()  # Display the current date and time
    
    # Prompt the user for the number of days
    try:
        days = int(input("Enter the number of days to add: "))
        calculate_future_date(days)  # Calculate and display the future date
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
