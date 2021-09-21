import csv
with open("Data.csv") as f9:
    reader=csv.reader(f9)
    file_data=list(reader)

file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    P1=file_data[i][1]
    newdata.append(float(P1))
N=len(newdata)
Total=0
for f in newdata:
    Total=Total+f
Mean=Total/N
print("Mean= "+str(Mean))