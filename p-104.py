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
modeRange = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

for height,occurence in data.items():
    if 75<float(height)<85:
        modeRange["75-85"]= + occurence
    elif 85<float(height)<95:
        modeRange["85-95"] = + occurence
    elif 95<float(height)<105:
        modeRange["95-105"] = + occurence
    elif 105<float(height)<115:
        modeRange["105-115"] = + occurence
    elif 115<float(height)<125:
        modeRange["115-125"] = + occurence
    elif 125<float(height)<135:
        modeRange["125-135"] = + occurence
    elif 135<float(height)<145:
        modeRange["135-145"] = + occurence
    elif 145<float(height)<155:
        modeRange["145-155"] = + occurence
    elif 155<float(height)<165:
        modeRange["155-165"] = + occurence
    elif 165<float(height)<175:
        modeRange["165-175"] = + occurence


mode_range, mode_occurence = 0,0
for range, occurence in modeRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode:-"+str(mode))
