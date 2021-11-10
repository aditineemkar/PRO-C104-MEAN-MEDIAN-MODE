import csv
with open ('SOCR-HeightWeight.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)
from collections import Counter

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

n = len(new_data)

#mean
total = 0 
for x in new_data:
    total=float(total)+float(x)

mean= total/n
print("Mean:-"+str(mean))


#median
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n//2 - 1])
    median2 = float(new_data[n//2])
    median = (median1 + median2)/2 
else:
    median = float(new_data[n//2])
print("Median :-"+str(median))



#mode 
data = Counter(new_data)
modeRange = {"50-60":0,"60-70":0,"70-80":0}

for height,occurence in data.items():
    if 50<float(height)<60:
        modeRange["50-60"]= modeRange["50-60"] + occurence
    elif 60<float(height)<70:
        modeRange["60-70"] = modeRange["60-70"] + occurence
    elif 70<float(height)<80:
        modeRange["70-80"] = modeRange["70-80"] + occurence

mode_range, mode_occurence = 0,0
for range, occurence in modeRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode:-"+str(mode))