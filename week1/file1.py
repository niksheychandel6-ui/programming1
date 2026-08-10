course1=float(input("Enter Course1 mark :"))
course2=float(input("Enter Course2 mark :"))
course3=float(input("Enter Course3 mark :"))
course4=float(input("Enter Course4 mark :"))

average=(course1+course2+course3+course4)/4

if average >= 85:
    grade ="A"
    remark ="Excellent"
elif average >=70:
    grade="B"
    remark =" Very Good"
elif average >=60:
    grade="C"
    remark ="Good"
elif average >=50:
    grade="D"
    remark =("Pass")
else:
    grade="F"
    remark =("Fail")
print("-----student result-----")
print("Course1:", format(course1,","))
print("Course2:", format(course2,","))
print("Course3:", format(course3,","))
print("Course4:", format(course4,","))

print("Final Grade:",grade)
print("Grade")
print("Remark:",remark)



