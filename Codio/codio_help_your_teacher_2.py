def get_count_faling_grades(student_info):
    """checks, if one or both of the two student grades
    are under 55.
    Gives back 1 or 2 if 1 or 2 grades ar under 55

    Args:
        student_info(dict): student info

    Returns:
        count_faling_grades(int): how many grades are under 55 (0, 1 or 2)

    """
    math_grade = student_info["math grade"]
    english_grade = student_info["english grade"]
    count_failng_grades = 0
    if math_grade < 55 and english_grade < 55:
        count_failng_grades = 2
    if math_grade < 55 or english_grade < 55:
        count_failng_grades = 1
    return count_failng_grades


def get_key_and_val_from_student_info(student_info) -> tuple:
    """looks of the vals of math_grade and english_grade
    if the vals are < 55, the var failing_grade is += 1
    gives back a tuple of the student name and his count of failng grades

    Args:
        student_info(dict): dictionary of student info

    Returns:
        student_name(str): name of student
        faling_grades(int): count of faling grades
    """
    student_name = student_info["student"]
    count_faling_grades = get_count_faling_grades(student_info)
    return student_name, count_faling_grades


def print_failing_grades(students):
    """gets as input a dict with stutend info
    takes the grades of each student and checks, if grade is failed
    gives back a dict, where each key is student name
    and each value the num of faling grades

    Args:
        students(list): list of dict with student info

    Returns:
        failing_grades(dict): dict of student name as key
        and failing grades as value:{
        student_name1 : failing_grades,
        student_name2 . failing_grades
        }
    """
    print("\nFailing grades per student:")
    failing_grades = {}
    for student_info in students:
        student_name, faling_grade = get_key_and_val_from_student_info(student_info)
        failing_grades[student_name] = faling_grade
        count_faling_grade = failing_grades[student_name]
        print(f"{student_name}: {count_faling_grade} faling grade(s)")


def get_all_grades_from_subject(subject:str, students:list) -> list:
    grade_list = []
    subject_key = subject + " grade"
    for dict in students:
        grade_list.append(dict[subject_key])
    return grade_list


def print_average_grades(students:list) -> dict:
    """Takes all grades from the list of dicts and calculates
    the average of math and english grades and the average
    all grades.

    Args:
        students(dict): list of dicts

    Returns:
        general_average_grades(dict): a dict, with three keys:{
        English : average(float),
        Math : average(float),
        Overall average : average(float)
        }
    """
    math_grades = get_all_grades_from_subject("math", students)
    english_grades = get_all_grades_from_subject("english", students)
    average_math = sum(math_grades) / len(math_grades)
    average_english = sum(english_grades) / len(english_grades)
    over_all_average = sum(math_grades + english_grades) / (len(math_grades) + len(english_grades))
    print(f"\nAverage grades per subject:\n"
          f"English: {average_english}\n"
          f"Math: {average_math}\n\n"
          f"Overall average grade across all subjects: {over_all_average}")


def make_list_of_grades(student_info:dict) -> list:
    """gets the grades from given dictionary(student_info)
    with slicing and puts the grades in a list

    Args:
         student_info(dict): single dict with student info

    Returns:
        grade_list(list): list of all grades from student
    """
    grade = "grade"
    grade_list = []
    for key in student_info:
        if key[-5:] == grade:
            grade_list.append(student_info[key])
    return grade_list


def get_best_grade(grades) -> float:
    """Takes a list of numbers and gives back the highest number

    Args:
        grades(list): list of grades

    Returns:
        best_grade(float): best grade in list of grades
    """
    best_grade = 0
    for grade in grades:
        if grade > best_grade:
            best_grade = grade
    return best_grade


def print_student_info(students):
    """Takes a list of student dictionaries as an argument,
    and print out the student’s name, best grade and average grade

    Args:
        students(list): a list with dict of student infos

    Output:
        prints the student infos from the dicts for each student
    """
    print("\nstudent Information:")
    for dict in students:
        student_name = dict["student"]
        grade_list = make_list_of_grades(dict)
        average_grade = sum(grade_list) / len(grade_list)
        best_grade = get_best_grade(grade_list)
        print(
            f"student: {student_name}, "
            f"Best Grade: {best_grade}, "
            f"Average Grade: {average_grade}"
        )


def make_student_info_list() -> list:
    """takes an input from User(int)
    executes "get_student_info()" with in the range of unser input

    Returns:
        student_info_list(list): list of dicts of student info
    """
    while True:
        try:
            students_count = int(input("Enter the number of students: "))
            student_info_list = []
            for i in range(students_count):
                print(f"\nEnter details for student {i + 1}:")
                student_info_list.append(get_student_info())
            break
        except ValueError:
            print("Excpected a number")
    return student_info_list


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
    """
    takes a number(int) for times of dicts, in student_list
    """
    student_info_list = make_student_info_list()
    print_student_info(student_info_list)
    print_average_grades(student_info_list)
    print_failing_grades(student_info_list)


if __name__ == "__main__":
    main()