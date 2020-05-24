text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find(":")
string = text[pos1+1:]
print(float(string.strip()))