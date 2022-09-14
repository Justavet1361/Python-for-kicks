#prompt for file name, Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
floatsum = 0
#search for substring and count them
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
# extract the float
    indst = line.find(":")
    extract = line[indst+3:]
    flextract = float(extract)
# compute the average
    floatsum = floatsum + flextract
    floatave = floatsum/count
# print the results
print('Average spam confidence:', floatave)
