# Prompt user input for hours and pay rate, and convert to float
hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")
h = float(hrs)
r = float(rate)
# calculate regular pay
if h < 40:
    pay = h * r
# calculate pay if there is overtime
elif h >= 40:
    pay = 40 * r + ((h-40) * (r *1.5))
    print ("You earned overtime!")
# output calculated wages
print ("Wages Earned: ", pay)
