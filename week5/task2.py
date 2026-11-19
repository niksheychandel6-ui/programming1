User_info={}
while True:
    name=input("Enter name:")
    if name=="stop":
        break
    phone=input("Enter phone number:")
    User_info[name]=phone
print("phone book")