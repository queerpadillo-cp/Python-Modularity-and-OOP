def get_student_name():
    """Asks and returns the student's name."""
    return input("Enter Student Name: ")


def get_term_grades():
    """Asks for grades per term and returns them in a dictionary."""
    prelim = float(input("Enter Prelim Grade: "))
    midterm = float(input("Enter Midterm Grade: "))
    final = float(input("Enter Final Grade: "))
    return {"prelim": prelim, "midterm": midterm, "final": final}