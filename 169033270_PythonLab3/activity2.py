num_grade = float(input("What is your numeric grade? ")) ###allows user to input their grade percentage
if num_grade >= 90 : ###defines grade range
    letter_grade = "A+" ###assigns letter grade to given range
    print(f"Your letter grade is {letter_grade}") ###prints user letter grade
elif num_grade >= 80 :
    letter_grade = "A"
    print(f"Your letter grade is {letter_grade}")
elif num_grade >= 70 :
    letter_grade = "B"
    print(f"Your letter grade is {letter_grade}")
elif num_grade >= 60 :
    letter_grade = "C"
    print(f"Your letter grade is {letter_grade}")
elif num_grade >= 50 :
    letter_grade = "D"
    print(f"Your letter grade is {letter_grade}")
elif num_grade <= 50 : 
    letter_grade = "F"
    print(f"Your letter grade is {letter_grade}")
    