def calculate_average(**kwargs):
    total = 0
    for score in kwargs.value():
        total=total+score
        average=total/len(kwargs)
        print("Average Score=",average)
        calculate_average(
            IT5014=60,
            IT7809=80,
            IT6789=50,
            IT5048=70
        )