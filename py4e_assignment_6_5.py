text = "X-DSPAM-Confidence:    0.8475"
indst = text.find(":")
extract = text[indst+3:]
flextract = float(extract)
print(flextract)
