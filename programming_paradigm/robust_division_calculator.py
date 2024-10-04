def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input. Please enter valid numbers."
