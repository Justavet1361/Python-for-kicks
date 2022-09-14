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

# calculate regular pay
regpay = 40 * r
if h < 40:
    otpay = 0
# calculate pay if there is overtime
elif h >= 40:
    otpay = (h-40) * (r *1.5)
pay = regpay + otpay
# output calculated wages
print (pay)
