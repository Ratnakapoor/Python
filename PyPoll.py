# Declare a csv file and Read the csv file 

import os
import csv
Candidate = []
Count = {}
total_votes = 0 
   
csv_path = os.path.join('election_data.csv')

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",") 
    
    csv_header = next(csv_reader)
    data = [row for row in csv_reader] 
    
    for row in data:
        total_votes += 1  
        name = row[2]
        if name not in Candidate:
            Candidate.append(name)
            Count[name] = 0 
           
        Count[name] = Count[name] + 1     
    
#Print Result on terminal and file 
file = open("PyPoll.txt", "w")

line3 = ("-------------------------------------------")
print(line3)
file.write(line3)
        
line1 = "Total Votes : " + str(total_votes) + '\n'  
print(line1)
file.write(line1)
    
prev_cnt = 0 
for i, j in Count.items():
        if ( prev_cnt < j) :
             winner = i 
        perct =  ((j / total_votes) * 100 )   
        line2 = str(i) + " : " +  str(round(perct, 3)) + "%  " +  str(j) + '\n'
        print(line2)
        file.write(line2)
        prev_cnt = j 
              

print(line3)
file.write(line3)
    
line4 = "Winner : " + str(winner) + '\n'
print(line4)
file.write(line4)

print(line3)
file.write(line3)

file.close() 
    
