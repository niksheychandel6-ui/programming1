while True:
     score= int(input("enter your score:"))
     if 0<=score<=100:
         break
     else:

         #print("Your score is invalid")
         if score >=80:
             print("Grade: A")
         elif score >=60:
             print("Grade: B")
         elif score >=50:
             print("Grade: C")
         else:



             print("Fail")


