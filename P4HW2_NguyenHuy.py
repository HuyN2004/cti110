# CTI-110
# P4HW2 - Pizza Order
# Huy Nguyen
# 5/9/2022
#
import math
# Ask user to enter number of students she/he would like to order pizza for.
while(True):
    student_count = int(input("How many students do you want to order pizza for? "))
    # Ask user for number of people that will be sharing each pizza ( 1.5, 2 or 3).
    pizza_count = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
    #Display result if user enter corrector not
    
    #this loop will repeat until user enter a valid pizza count 1.5,2 or 3
    while pizza_count not in [1.5,2,3]:
        print ('\nINVALID ENTRY !!!!')
        print ('Should have entered 1.5, 2 or 3')
        print ()
        pizza_count = float(input('Enter number of people per pizza again.(1.5, 2 or 3): '))
    #Caculate the number of Whole pizzas if user enters 1.5, 2 ,3
    pizza_count = student_count / pizza_count
    #Caculate total price by take pizza_per mutiply price of pizza is $5
    total_price = float(pizza_count * 5)
    # Caculate tax by 6%
    tax = total_price * 0.06
    #Display information and caculate total price plus tax
    print('\n----Pizza Order--------')
    print('Number of Students:', student_count)
    print('Pizzas Needed:', math.ceil(pizza_count))
    print(f'Price ${(total_price + tax):.2f}')
    print('------------------------')
    prog_reset = (input('\nWould you like to run program again (y for yes): '))
    if prog_reset == 'y':
        continue
    else:
        break

