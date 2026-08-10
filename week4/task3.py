print("-----------------")
scores=[65,72,80,55,90,68,77]
above_70_count =0
for score in scores:
    if score>70:
        above_70_count+=1

print("students scoring above 70 : ",above_70_count)
for score in scores:
    if score>=60:
        print(score,"pass")
    else:
        print(score,"fail")
print("-----------------")
