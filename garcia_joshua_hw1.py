# Name: Josh Garcia 
# Section: C
# Description: The loan calculator tells you how much money you have to repay over the life of a loan.

print("\n Welcome! to the Loan Calculator!")
print(" Please enter information below")
print("----------------------------------")
#Creating my variables that I will grab input from user and then use to calculate the loan
principal = (input(' How much money, do you still have left in loan? : '))
years = int(input(' How many years do you have left required to repay the loan? : '))
rate = (input(' What is the intrest rate on the loan? : '))

#print user inputs
print('\n Principle: {}\n Rate: {}\n Years: {}'.format(principal,rate,years))

#created two if statements that will check if there is a $ or %, and then removing it, so we can preform calculations
if principal[0] == "$":
    principal = float(principal[1:])
else:
    principal = float(principal)

if rate[-1] == "%":
    rate = float(rate[:-1])/100
else:
    rate = float(rate)

#This will calculate the input given from the user
payment = float( (((1+rate)**years)*principal*rate)/(((1+rate)**years)-1) )

#displaying the results using the print() method
print('\n Annual payment = ${:,.2f}'.format(payment))

#calculating and print() the results of monthly payment
monthly = float(payment/12)
print(' Monthly payment = ${:,.2f}'.format(monthly))

#Calculating and print() the results of total paid of loan
total_payment = float(payment*years)
print(' Total paid for the life of the loan = ${:,.2f}'.format(total_payment))

#Here I ask user for annual income, so I can compare user monthly income with monthly payment.
user_salary = input("\n Please enter your annual income: ")

#if user uses $ sign, this if statement will remove it
if user_salary[0] == "$":
    user_salary = float(user_salary[1:])
else:
    user_salary = float(user_salary)

#if statement will spit out whether user needs to refinance or they are on track to pay off loan 
if (user_salary/12) < monthly:
    if rate > .05:
        print("\n Yikes! You should refinance! Please seek financial counseling.\n")
else:
    print("\n Awesome! If you make all your payments, \n you will get your loan paid off in time!\n")
