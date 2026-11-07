#classify scores using the grading scheme supplied for the excercise.

student_name = input("Enter the sudent's name:")
score = float(input("Enter the score from 0 to 100:"))


if score < 0 or score > 100:
    print("invalid score.The score must be betweeen 0 and 100.")
else:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
         grade = "D"
    elif score >= 30:
        grade = "E"
    else:
        grade = "F"
    
    print()
    print("STUDENT RESULT")
    print("===============")
    print(f"Name:{student_name}")
    print(f"Score:{score:.2f}")
    print(f"Grade:{grade}")
