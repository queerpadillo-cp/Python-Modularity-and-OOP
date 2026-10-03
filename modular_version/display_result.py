def display_summary(name, grades, average):
    """Prints the final summary."""
    print("\n--- STUDENT GRADE REPORT ---")
    print(f"Name: {name}")
    print(f"Prelim: {grades['prelim']:.2f}")
    print(f"Midterm: {grades['midterm']:.2f}")
    print(f"Final: {grades['final']:.2f}")
    print(f"Average: {average:.2f}")
    print("----------------------------")