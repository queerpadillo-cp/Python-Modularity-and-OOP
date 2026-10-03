from student import Student


def main():
    name = input("Enter Student Name: ")

    # Create an instance (Object) of the Student class
    student1 = Student(name)

    # Execute methods
    student1.ask_grades()
    student1.calculate_average()
    student1.display_info()


if __name__ == "__main__":
    main()