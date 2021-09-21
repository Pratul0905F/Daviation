from Mean import Total
import math
import csv
with open("Data.csv") as TTP:
    reader=csv.reader(TTP)
    lister=list(reader)
data=lister[0]
def Mean(data):
    lenght=len(data)
    total=0
    for x in data:
        total=total+int(x)
    m=total/lenght
    return m
squarelist=[]
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squarelist.append(a)
sum=0
for j in squarelist:
    sum=sum+i
result=sum/len(data)-1
STD=math.sqrt(result)
print(STD)