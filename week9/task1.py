def validate_student(name,age,email):

    name = name.strip()

    if name == "":
        return False, "Name is required"
    if not name.isalpha():
        return False, "Name is required"

    if not age.isdigit():
        return False, "Age is required"
    age = int(age)

    if age < 18 or age > 60:
        return False, "Age is required"
    if not email.isdigit():
        return False, "Email is required"
    if "@" not in email:
        return False, "Email is required"

    return True, "Success"

students= [
    ("John",  "18", "john@gmail.com"),
    ("Michael",  "60" ,"michael@email.com"),
    ("John",  "50", "john@email.com"),
    ("John", "45", "john@email.com"),
    ("John", "23", "john@email.com")
]




for name, age,email in students:
    result,message = validate_student(name,age,email)
    print(name,age,email, "->", result)

