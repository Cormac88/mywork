# Roundiong percentages

# Author: Comrac Hennigan

grade = float(input("Enter the percentage: "))
gradeRounded = round(grade) # The grade is rounded up to the nearest whole number

if gradeRounded < 0 or gradeRounded > 100:
    print ("Please enter a number between 0 and 100")
elif gradeRounded < 40:
    print ("Fail")
elif gradeRounded < 50:
    print ("Pass")
elif gradeRounded < 60:
    print ("Merit 2")
elif gradeRounded < 70:
    print ("Merit 1")
else:
    print ("Distinction")