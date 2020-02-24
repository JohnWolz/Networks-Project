import sys
import csv

file = 'topology.csv'

input_data=[]
readCSV = csv.reader(open(file), delimiter=',')
i = 0
for row in readCSV:
    input_data.append(row)
    input_data[i].remove(input_data[i][0]) # shaves off first column
    i+=1

print(input_data)
