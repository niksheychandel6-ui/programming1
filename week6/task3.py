def print_results(students):
    for name, mark in students.items():
        if mark >=60:
            print(name,mark,"PASS")
        else:
            print(name,mark,"FAIL")


students ={
    "JOHN":65,
    "MARY":82,
    "ALI":55,
    "SINA":90,
}
print_results(students)
