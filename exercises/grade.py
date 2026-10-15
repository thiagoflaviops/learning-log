test_score = float(input("Enter your test score: "))

if test_score > 100 or test_score < 0:
    print("The score must be between 0 and 100.")
else:
    if test_score >= 90:
        letter_grade = "A"
    elif test_score >= 80:
        letter_grade = "B"
    elif test_score >= 70: 
        letter_grade = "C"
    elif test_score >= 60:
        letter_grade = "D"
    else: 
        letter_grade = "F"

    print(f"Your grade is: {letter_grade}")