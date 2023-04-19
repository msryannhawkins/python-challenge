#import OS and csv
import os

import csv

#set up and direct to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

#Read actual CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print (csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)