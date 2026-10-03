class Student:
    def __init__(self, name):
        # Attributes
        self.name = name
        self.grades = {}
        self.average = 0.0

    # Behavior / Methods
    def ask_grades(self):
        prelim = float(input("Enter Prelim Grade: "))
        midterm = float(input("Enter Midterm Grade: "))
        final = float(input("Enter Final Grade: "))
        self.grades = {"prelim": prelim, "midterm": midterm, "final": final}

    def calculate_average(self):
        if self.grades:
            self.average = sum(self.grades.values()) / len(self.grades)
        return self.average

    def display_info(self):
        print("\n--- STUDENT GRADE REPORT (OOP) ---")
        print(f"Name: {self.name}")
        for term, grade in self.grades.items():
            print(f"{term.capitalize()}: {grade:.2f}")
        print(f"Average: {self.average:.2f}")
        print("---------------------------------")