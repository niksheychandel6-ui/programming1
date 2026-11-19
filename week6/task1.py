def check_result(mark):
    if mark >= 60:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

marks = [55, 70, 62, 40, 90]
for m in marks:
    check_result(m)