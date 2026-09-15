def student_grade():
    student_grade = int(input("Enter grade: "))
    if student_grade >= 90:
        return ("A")
    elif student_grade >= 80:
        return ("B")
    elif student_grade >= 70:
        return ("C")
    elif student_grade >= 60:
        return ("D")
    elif student_grade >= 50:
        return ("F")
    else:
        return ("No grade inputed")

def main():
    result = student_grade()
    print(result)

main()
    
