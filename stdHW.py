import csv
import math

with open('stdData.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

sum = 0
length = len(data)
for i in data:
    sum+=int(i[0])

mean  = sum/length

sumSTD = 0
a = 0
for x in data:
    a = float(x[0])
    sumSTD+=(a-mean)^2

std = math.sqrt(sumSTD/length)
print(std)