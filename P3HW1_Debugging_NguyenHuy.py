# I was supposed to put a comment here
# My Last Name

def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50 
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    
    if score >= B_score:
        print('Your grade is: B')

    if score >= C_score:
        print('Your grade is: C')

    if score >= D_score:
        print('Your grade is: D')
    
    if score >= F_score: 
        print ('Your grade is: F') # TO DO: finish this

    print(score)

# program start
main()
