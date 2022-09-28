# Designed by Tamara Lynch: Week 6 In Class Assignment #1 26 September 2022.

# Spherical Inc. sells baseballs for $1.99 each. 
# However, discounts are given according quantities listed in the following table:

# Quantity	    Discount
#   0 - 9	    0%
#  10 - 50	    5%
#  51 or more	10%

# Establish the constants
BASEBALL_PRICE  = 1.99
GIFT_WRAP       = 2.00
TAX             = 0.06
DISCOUNT_1      = 0.05
DISCOUNT_2      = 0.10

# prompt the user to enter the number of baseballs purchased.
# ask the user if they want giftwrapping.

baseball_qty = int(input('How many baseballs would you like to purchase?  '))
wrapped = input('Would you like to have your purchase gift wrapped? (Please enter y for yes or n for no.)  ')

# Determine the discount and subtotal based on the quantity requested.
subtotal = 0
 
if baseball_qty <= 9:
    subtotal = baseball_qty * BASEBALL_PRICE 
    discount_statement = ('if you were to purchase 10 or more, you get a discount!')
elif 10 <= baseball_qty <= 50:
    subtotal = baseball_qty * (BASEBALL_PRICE-(BASEBALL_PRICE * DISCOUNT_1))
    discount_statement = ('you received a discount of: ' + str(DISCOUNT_1  * 100) + '% off each baseball')
elif baseball_qty >= 51:
    subtotal = baseball_qty * (BASEBALL_PRICE-(BASEBALL_PRICE * DISCOUNT_2))
    discount_statement = ('you received a discount of: ' + str(DISCOUNT_2  * 100) + '% off each baseball')

# Include tax of 6% on the total of the purchase, excluding giftwrapping.
sales_tax = subtotal * TAX
total = subtotal + sales_tax

# The program should display the amount of the discount (if any) 
#   and the total amount of the purchase after the discount 

print('You requested a quantity of ' + str(baseball_qty) + ' baseballs')
print('The cost of your baseball(s) is: ${:.2f}'.format(subtotal) + ' and ' + discount_statement)

# If user elected giftwrapping, add the cost of wrapping.
if wrapped == 'y':
    amt_due = total + GIFT_WRAP
    print('You chose to have your purchase giftwrapped.')
    print('The cost of gift-wrapping is ${:.2f}'.format(GIFT_WRAP))
else:
    amt_due = total
    print('You chose not to have your purchase giftwrapped.')
    

print('Your sales tax is: ${:.2f}'.format(sales_tax))
print('Your total purchase price due is: ${:.2f}'.format(amt_due))