from get_inputs import get_student_name, get_term_grades
from grade_calculator import calculate_average
from display_result import display_summary

def main():
    name = get_student_name()
    grades = get_term_grades()
    average = calculate_average(grades)
    display_summary(name, grades, average)

if __name__ == "__main__":
    main()