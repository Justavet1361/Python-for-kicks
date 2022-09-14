largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if largest is None:
        largest = int(num)
    if smallest is None:
        smallest = int(num)
    if num == "done" : break
    try:
        int(num)
    except:
        print("Invalid Input")
        continue
    if int(num) > int(largest):
        largest = num
    if int(num) < int(smallest):
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)
