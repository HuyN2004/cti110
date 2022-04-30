# CTI-110
# P3HW2 - Pizza Order
# Your Name 
# Date
#
# Ask user to enter number of students she/he would like to order pizza for.
student_num = int(input("How many students do you want to order pizza for? "))
# Ask user for number of people that will be sharing each pizza ( 1.5, 2 or 3). 
pizza_per = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
#Caculate the number of Whole pizzas if user enters 1.5, 2 ,3 
if (pizza_per == 1.5) or (pizza_per == 2) or (pizza_per == 3): 
    pizza_per = student_num / pizza_per
    #Caculate total price by take pizza_per mutiply price of pizza is $5 
    total_price = float(pizza_per * 5) 
    #Caculate tax by 6%
    tax = total_price * 0.06 
    #Display information and caculate total price plus tax
    print('----Pizza Order--------')
    print('Number of Students:', student_num)
    #Import ceil from math
    from math import ceil
    print('Pizzas Needed:', ceil(pizza_per))
    print('Price $', total_price + tax)
#If user enters a value other than 1.5, 2 or 3, this program will display error and tell user to run the program again
else:
    print ('INVALID ENTRY !!!!/n')
    print ('Should have entered 1.5, 2 or 3')
    print ()
    print ('Run Program Again')
