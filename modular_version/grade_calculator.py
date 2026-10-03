def calculate_average(grades):
    """Calculates and returns the average grade."""
    total = sum(grades.values())
    return total / len(grades)