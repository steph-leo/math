score = float(input("Enter student scores: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B" 
elif score >= 70:
    grade = "C" 
else:
    grade = "F"
print("The score is: ",grade)