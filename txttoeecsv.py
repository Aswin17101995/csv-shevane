import csv
myfile=open("shiva.txt",'r')
s=myfile.readlines()
li=s[0].split(" ")
final=[]
for i in range(1,len(li)):
    temp=[]
    temp.append(li[i])
    final.append(temp)
print(final)
with open('shevane.csv','w',newline='')as f:
    wri=csv.writer(f)
    wri.writerows(final)
