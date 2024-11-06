def get_student_info() -> dict:
    """Takes 3 inputs from the user
    1. Students_name
    2. english_grade
    3. math_grade

    Returns:
        student_information(dict): {
        student : student_name,
        english_grade : float
        math_grade : float
        }
    """
    student_information = {}
    student_information["student"] = input("Enter students name: ")
    student_information["english grade"] = get_grade("english")
    student_information["math grade"] = get_grade("math")
    return student_information


def get_grade(subject:str) -> float:
    """Takes as arg a subject
    asks the user for an input(Grade, type:number)
    if the input is not a number, prints: "Expected a number"
    asks the user again for an input

    Args:
        subject(str): f.example: English

    Returns:
         grade(float): the grade of the subject
    """
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: "))
            return grade
        except ValueError:
            print("Expected a number")


def main():
    print(get_student_info())

if __name__ == "__main__":
    main()