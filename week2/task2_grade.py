print("-----STUDENT RESULT-----")
AssignmentMark=float(input("Enter Assignment Mark/100"))
TestMark=float(input("Enter Test Mark/100"))
ExamMark=float(input("Enter Exam Mark/100"))
print("AssignmentMark",AssignmentMark)
print("TestMark",TestMark)
print("ExamMark",ExamMark)
AssignmentContribution=AssignmentMark/100*30
TestContribution=TestMark/100*30
ExamContribution=ExamMark/100*40
print("AssignmentContribution",AssignmentContribution)
print("TestContribution",TestContribution)
print("ExamContribution",ExamContribution)
FinalGrade=AssignmentContribution+TestContribution+ExamContribution
print("FinalGrade",FinalGrade)
print("-------------------------")
