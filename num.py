num = [1,2,3]
file = open("namba.txt",'w')
for i in num:
    file.write(str(i) + "\n")
file.close()
