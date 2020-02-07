
print("This program going to check if student has been approved or has been failed")
#Data validation

#1st grade validation:
data_valid = False

while data_valid == False:
    grade1 = float(input("Type your 1st test grade: "))
    if grade1 < 0 or grade1 > 10:
        print("Grade format is 0 to 10")
        continue
    else:
        data_valid = True

        
#2nd grade validation:        
data_valid = False

while data_valid == False:
    grade2 = float(input("Type your 2st test grade: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade format is 0 to 10")
        continue
    else:
        data_valid = True

#total classes validation:
data_valid = False

while data_valid == False:
    total_classes = int(input("Type the number of classes: "))
    if total_classes <= 0:
        print("Can't be 0 or less classes")
        continue
    else:
        data_valid = True

#absences validation
data_valid = False

while data_valid == False:
    absences = int(input("Type the number of absences: "))
    if absences < 0 or absences > total_classes:
        print("Can't be minus absences or more than total classes")
        continue
    else:
        data_valid = True         

#average
avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences ) / total_classes

#printing values
print("Average grade: ", avg_grade)
print("Attendance : ", str(round(attendance * 100,2)) + "%")

#conditions for aprove or for fail
if(avg_grade >= 6):
    if(attendance >= 0.8):
        print("The student was approved")
    else:
        print("The student was failed due to low attendance")
elif (attendance >= 0.8):
    print("The student was failed due to an average grade lower than 6")
else:
    print("The student failed due to an low attendance and low avg grade")
