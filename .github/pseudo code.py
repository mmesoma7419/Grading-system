START
Prompt user to enter score
Read score

IF score is between 70 and 100 THEN
    grade = "A"
ELSE IF score is between 60 and 69 THEN
    grade = "B"
ELSE IF score is between 50 and 59 THEN
    grade = "C"
ELSE IF score is between 45 and 49 THEN
    grade = "D"
ELSE IF score is between 40 and 44 THEN
    grade = "E"
ELSE IF score is between 0 and 39 THEN
    grade = "F"
ELSE
    grade = "Invalid score"

Display "Your grade is: " + grade
END