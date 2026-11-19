class ClubRegistration:

    def __init__(self):
        self.student_info = {}
        self.num_withdrawn = 0
        self.mem_id = 10001

    def register(self):

         while True:
            student_id = input("Enter student ID: ")

            if student_id == "":
                print("Student ID cannot be empty.")

            elif not student_id.isdigit():
                print("Student ID must contain numbers only.")

            elif len(student_id) != 4:
                print("Student ID must be 4 digits.")

            else:
                duplicate = False

                for student in self.student_info.values():
                    if student["student_id"] == student_id:
                        duplicate = True
                        break

                if duplicate:
                    print("Student ID already exists.")
                else:
                    break

        last_name = input("Enter last name: ")
        programme = input("Enter your programme (Diploma/Bachelor): ")

        membership_id = "AB" + str(self.mem_id)
        self.mem_id += 1

        self.student_info[membership_id] = {
            "student_id": student_id,
            "last name": last_name,
            "programme": programme
        }

        print("Successfully registered", membership_id)

    def withdraw(self):
        memberid = input("Enter your membership ID for withdraw: ")
        lname = input("Enter your last name: ")

        if memberid in self.student_info:

            if self.student_info[memberid]["last name"] == lname:
                del self.student_info[memberid]
                print("Withdrawn successfully", memberid)
                self.num_withdrawn += 1

            else:
                print("Incorrect last name - Access Denied")

        else:
            print("Incorrect membership ID")

    def display(self):

        for k, v in self.student_info.items():

            print("ID:", k)
            print("Student ID:", v["student_id"])
            print("Last Name:", v["last name"])
            print("Programme:", v["programme"])
            print()

    def summary(self):

        diploma = 0
        bachelor = 0

        for student in self.student_info.values():

            if student["programme"] == "Diploma":
                diploma += 1
            else:
                bachelor += 1

        print("Number Diploma:", diploma)
        print("Number Bachelor:", bachelor)
        print("Total Registered:", len(self.student_info))

    def menu(self):

        while True:

            print("\nClub Membership System")
            print("1: Registration")
            print("2: Withdraw")
            print("3: Display")
            print("4: Summary")
            print("5: Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.withdraw()

            elif choice == "3":
                self.display()

            elif choice == "4":
                self.summary()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")


club = ClubRegistration()
club.menu()