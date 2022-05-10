# CTI-110
# P5HW1 - Score List
# Huy Nguyen    
# 5/10/2022
#
#Asking for scores count 
count=int(input("How many scores do you want to enter? "))
#Assigning i and mylist
i, mylist=1, []
#Create loops
while(True):
    if(len(mylist)==count): 
        break
    print("Enter score #" + str(i) + ": ", end="")
    score = int(input())
    if(score<0 or score>100):
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    else:
        mylist.append(float(score))
        i += 1 
#Sorting the list 
mylist.sort()
lowest_score = mylist[0]
mylist.remove(lowest_score)
score_avg=sum(mylist) / len(mylist)
#Assign score_avg and grade
if(score_avg>90):
    grade = "A"
elif(score_avg>=80 and score_avg<90):
    grade = "B"
elif(score_avg>=70 and score_avg<80):
    grade = "C"
else:
    grade = "F"
#Results 
print("--------------Results-----------")
print("Lowest Score      :",lowest_score)
print("Modified List     :",mylist)
print("Scores Average    :",score_avg)
print("Grade             :",grade)
print("-----------------------------------")