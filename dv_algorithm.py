#################################################################
# Name: John Wolz, Stella Li, Nicole Robles
# Date: February 29, 2020
# Description: Distance-Vector Routing Algorithm
#################################################################

import sys
import csv

file = 'topology.csv'

# read CSV file and import data
input_data=[]
readCSV = csv.reader(open(file), delimiter=',')
i = 0
for row in readCSV:
    input_data.append(row)
    # shave off first column (labels)
    input_data[i].remove(input_data[i][0])
    i+=1
# removes first row (also labels)
input_data.remove(input_data[0])

def DistanceVector(input_data):
    for i in range (len(input_data)):
        for j in range(len(input_data[1])):
            # do not need to check distance between node and itself
            if int(input_data[i][j]) != 0: 

                # finds distance from start node to intermediate node and from intermediate node to end node
                intermediate_index = (j+1) % len(input_data[i])

                if int(input_data[i][intermediate_index]) == 0: # ensures the intermediate node is not the start node
                    intermediate_index = (j+2) % len(input_data[i])
                
                distance1 = int(input_data[i][intermediate_index])
                distance2 = int(input_data[intermediate_index][j])

                # compares distances
                if (distance1 + distance2 < int(input_data[i][j])):
                    input_data[i][j] = distance1 + distance2

    return input_data

new_distance_vectors = DistanceVector(input_data)

##################### PRINT #####################################
print("Distance vector for node x:",input_data[0])
print("Distance vector for node y:",input_data[1])
print("Distance vector for node z:",input_data[2])

