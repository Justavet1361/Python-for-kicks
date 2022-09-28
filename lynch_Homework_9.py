# Designed by Tamara Lynch: Week 6 In Class Assignment #3 26 September 2022.

# Write a program that calculates and prints the bill for a cellular telephone company.  
# The company offers two types of service: regular and premium. 
# Its rates vary, depending on the type of service. 
# 
# The rates are computed as follows:
 
# Regular Service:  

#   $10.00 plus
#   First 50 minutes are free, over that, $0.20 per minute.

# Premium service:  

#  $25.00 plus
#  For calls made from 6:00 a.m. to 6:00 p.m., the first 75 minutes are free, over that, $0.10 per minute.
#  For calls made from 6:00 p.m. to 6:00 a.m., the first 100 minutes are free, over that, $0.05 per minute.

# Your program should . 

# Constants

REG_PLAN_FEE = 10.00
REG_FREE_MIN = 50
PREM_PLAN_FEE = 25.00
REG_PER_MIN = 0.20
PREM_PER_AM_MIN = 0.10
PREM_PER_PM_MIN = 0.05
PREM_FREE_AM_MIN = 75
PREM_FREE_PM_MIN = 100

# prompt the user to enter an account number, a service code, and the number of minutes the service was used

acct_num = input('Please input your account number: ')
service = input('Please enter your service code:  R or r for the regular plan, p or P for the premium plan: ')
service = service.lower()


# Calculate the rates 
if service == 'r':
    minutes = int(input('Please enter the minutes used: '))
    if minutes > 50:
        reg_charge = (minutes - 50) * .20
        total = reg_charge + REG_PLAN_FEE
    else:
        reg_charge = 0
        total = reg_charge + REG_PLAN_FEE
elif service == 'p':
    minutes_day = int(input('Please enter the number of minutes used during the day hours of 6 am to 6 pm:  '))
    minutes_night = int(input('Please enter the number of minutes used during the evening/night hours of 6 pm to 6 am:  '))
    if minutes_day > PREM_FREE_AM_MIN:
        daytime_charge = (minutes_day - PREM_FREE_AM_MIN) * PREM_PER_AM_MIN
    else: 
        daytime_charge = 0
    if minutes_night > PREM_FREE_PM_MIN:
        nighttime_charge = (minutes_night - PREM_PER_PM_MIN) * PREM_PER_PM_MIN
    else: 
        nighttime_charge = 0
    total = daytime_charge + nighttime_charge + PREM_PLAN_FEE  
else:
    print('Sorry, you did not enter a correct service code')
   
# Your program should output the account number, type of service, 
# number of minutes the telephone service was used, and the amount due from the user.
print('\n\nAce Cellular Service Billing Statement\n__________________________________')
print('\nAccount Number:\t', acct_num)
if service == 'p':
    print('\nYou are enrolled in the Premium Plan')
    print('\nYour plan service fee is:   \t\t\t${:.2f}'.format(PREM_PLAN_FEE))
    print('\nThe rate for calls between 6 am and 6 pm is:\t ${:.2f}'.format(daytime_charge))
    print('\nThe rate for calls between 6 pm and 6 am is:\t ${:.2f}'.format(nighttime_charge))
    print('\nYour total bill is:   \t\t\t\t${:.2f}'.format(total))
elif service == 'r':
    print('\nYou are enrolled in the Regular Plan')
    print('\nYour plan service fee is: \t\t ${:.2f}'.format(REG_PLAN_FEE))
    print('\nThe rate for calls\n made over the first',REG_FREE_MIN,' minutes is: \t${:.2f}'.format(reg_charge))
    print('\nYour total bill is:   \t\t\t${:.2f}'.format(total))
else:  
    print('Please contact customer service for your billing information.') 