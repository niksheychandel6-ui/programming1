class Student :
    def __init__(self,name,course,marks) :
        self.name = name
        self.course = course
        self.marks = marks

    def display_Student(self) :
        print("Name:",self.name)
        print("Course:",self.course)
        print("Marks:",self.marks)


#Activity Answers Part 1.
#1.We would need to store a lot of information for each student such as their name ,course and marks
#2.Without OOP we might end up creating many seperate variables which would be difficult to organise
#3. Yes the programe will be very dificult .

#Activity Answers Part 2.
#1.The class is called Student
#2.__init__ is a constructor method.
#It runs automatically when a new student object is created
#.It assigns the name,course and marks to the student object.

student1 = Student("Ali","Cybersecurity",78)
student1.display_Student()
student2 = Student("Sara","IT dev",82)
student2.display_Student()
student3 = Student("John","Networking",83)
student3.display_Student()

#Activity 3
#Change student1's marks
student1.marks=90
#Display student1's updated info
student1.display_Student()

#Activity 3 Answers
#1.Because we used student1.marks
#2.Because marks belongs to each individual student object
#3.Because student2 has its own seperate marks values
