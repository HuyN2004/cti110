# Total Purchase Project
# 4/17/2022
# CTI-110 P2HW1 - Total Purchases
# Huy Nguyen    
#
#List of 5 input price
p1 = float(input("Enter the price of item #1: "))
p2 = float(input("Enter the price of item #2: "))
p3 = float(input("Enter the price of item #3: "))
p4 = float(input("Enter the price of item #4: "))
p5 = float(input("Enter the price of item #5: "))
#Calculate Subtotal 
subtotal = p1 + p2 + p3 + p4 + p5
# Calculate Sales Tax
taxes = subtotal / 7
#Calculate overall total
total= subtotal + taxes
#Result section
print("-------Results-------")
print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {taxes:.2f}')
print(f'Total: {total:.2f}')