# Prompt user input for hours and pay rate, and convert to float
hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print("Please enter a numerical value")
rate = input("Enter Pay Rate: ")
try:
    r = float(rate)
except:
    print("Please enter a numerical value")
# define the function to calculate overtime pay
def computepay(h,r):
    otpay = (h-40) * (r*1.5)
    return otpay
# calculate regular pay
regpay = 40 * r
if h < 40:
    otpay = 0
# calculate pay if there is overtime
elif h >= 40:
    computepay(h,r)
pay = regpay + computepay(h,r)
# output calculated wages
print (pay)
