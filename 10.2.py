name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for i in handle:
    if i.startswith("From") and len(i.split()) > 2:
        l = i.split()
        if not dic.has_key(l[5][:2]):
            dic[l[5][:2]] = 1
        else:
            dic[l[5][:2]] += 1
                
key = sorted(dic)
for i in key:
    print ("%s %d" % (i,dic[i]))