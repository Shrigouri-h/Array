maths=99
english=85  
science=78
history=88  
hindi=99
average = maths+english+science+history+hindi/ 5
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'
print("Average Marks:", average)
print("Grade:", grade)