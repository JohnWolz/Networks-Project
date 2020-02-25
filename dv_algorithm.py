import sys
import csv

file = 'topology.csv'

input_data=[]
readCSV = csv.reader(open(file), delimiter=',')
i = 0
for row in readCSV:
    input_data.append(row)
    input_data[i].remove(input_data[i][0]) # shaves off first column (labels)
    i+=1
input_data.remove(input_data[0]) # removes first row (also labels)

print(input_data)

def DistanceVector(input_data):
    for i in range (len(input_data)):
        for j in range(len(input_data[1])):
            if int(input_data[i][j]) != 0: # do not need to check distance between node and itself

                # finds distance from start node to intermediate node and from intermediate node to end node
                intermediate_index = (j+1) % len(input_data[i])
                distance1 = int(input_data[i][intermediate_index])
                distance2 = int(input_data[intermediate_index][j])

                # compares distances
                if (distance1 + distance2 < int(input_data[i][j])):
                    input_data[i][j] = distance1 + distance2

    return input_data

new_distance_vectors = DistanceVector(input_data)
print(new_distance_vectors)
