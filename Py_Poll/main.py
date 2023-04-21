#import OS and csv
import os

import csv

counter = 0
TV = 0

#set up and direct to csv file
csvpath = os.path.join('Py_Poll', 'Resources', 'election_data.csv')

#establish a candidate dictionary
CanDict = {}


#Read actual CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#for loop
    for row in csvreader:
        
        #Total Votes counter
        TV += 1 
        


        #identify where to pull candidate info from
        candidate = row[2]


        #if the candidate in CanDict is the same as before, add it to running votes
        #else, set it equal to 1 vote
        if candidate in CanDict: 
            CanDict[candidate] +=1

        else: 
            CanDict[candidate] = 1

#Find the most frequently names candidate to be the winner, key refers to the elements in the CanDict
    results = max([x for x in CanDict.values()])
    Winner = ""
    
    for key, val in CanDict.items():
        if val == results:
            Winner = key


print(TV)

#format the output into three rows with each correlating data point calculated above
for key,val in CanDict.items():  
        #print key, i.e. candidate name: percentage and individual's total vote count 
        print(f"{key}: {round(val/TV*100, 3)}% ({val})")

print(Winner)
        




