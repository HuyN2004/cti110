# BOOM Score Average
# 4/17/2022
# CTI-110 P2HW1 - Score Average
# Huy Nguyen    
#
#BOOM SCORE
print('BOOM SCORE')
#Create 7 input score
s1 = float(input("Enter score #1: "))
s2 = float(input("Enter score #2: "))
s3 = float(input("Enter score #3: "))
s4 = float(input("Enter score #4: "))
s5 = float(input("Enter score #5: "))
s6 = float(input("Enter score #6: "))
s7 = float(input("Enter score #7: "))
#Create a list base on input
score_list = [s1, s2, s3, s4, s5, s6, s7]
#Find the lowest number
lowest = min(score_list)
# Remove the lowest score from the list
score_list.remove(lowest)
#Calculate Average
average = sum(score_list) / 7
#Result 
print("-------Results-------")
print(f'Lowest Score: {lowest:.2f}')
print(f'Modified List: {score_list}')
print(f'Scores Average: {average:.2f}')