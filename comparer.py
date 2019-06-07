f1=open("Bureau/python/comparer/test1.txt","r")
f2=open("Bureau/python/comparer/test2.txt","r")

lineNum= 0

for line1 in f1:
    for line2 in f2:
        if line1==line2:
            lineNum += 1
            print("Line number " + str(lineNum) + " it's the same\n")
        else:
            lineNum += 1
            print("DIFFERENCE ON LINE N." + str(lineNum) + "\n\n" + "First version = " + line1 + "\n" + "Second version = " + line2)
        break
f1.close()
f2.close()
