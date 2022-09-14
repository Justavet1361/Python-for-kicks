# prompt user to enter a score
score = input("Enter Score between 0.0 and 1.0: ")
# ensure that it is an input that can be converted to a float
try:
    iscore = float(score)
except:
    print ("Please enter a numerical score:")
    score = input("Try again: ")
    iscore = float(score)
# ensure the input falls in the required range
iscore < 0.0 or iscore > 1.0
print ("Please enter a score between 0.0 and 1.0")
score = input("Try again: ")
iscore = float(score)
# print the corret letter score
if iscore >= 0.9:
    print ("A")
elif iscore >= 0.8:
    print ("B")
elif iscore >= 0.7:
    print ("C")
elif iscore >= 0.6:
    print ("D")
else:
    print ("F, Sorry, you failed miserably")
