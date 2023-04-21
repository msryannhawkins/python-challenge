#import OS and csv
import os

import csv

#set up and direct to csv file
csvpath = os.path.join('Py_Bank', 'Resources', 'budget_data.csv')
print(csvpath)

#use an array, use list--build list ith loop first to get data into a dictionary, then put it into the loop. 
#First create variables then use .append within for loop
#Month Variable: create list for months
months = []

#Profit/Loss Variable: create list for the profits and losses
profitloss = []

#Change Variable: create list for monthly change of profits and losses, set total to 0
change = []
total = 0

#Read actual CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #forloop
    for row in csvreader:
        #set 0 to monthly row; use append to add to end of list
        months.append(row[0])
        #set 1 to profits and losses row due to the first row not shoing profit/loss bc initial value
        profitloss.append(row[1])
        #add the value to each row to create a running total
        total += int(row[1])

#month to month profits and losses change value calculation loop
#subtract a month from months because the first row does not show change as stated before
    for nr in range(len(months)-1):
        change.append(int(profitloss[nr+1]) - int(profitloss[nr]))

    #greates increase and decrease with .index to locate the max and min value related to change
    GrInc = change.index(max(change))
    GrDec = change.index(min(change))

    #match months to greatest increase and decrease and give srtings a new variable
    DateMax = months[GrInc]
    DateMin = months[GrDec]

    #change value average and round result
    ChngAvg = round(int(sum(change))/(int(len(months))-1),2)

print("Financial Analysis")
print("---------------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total}')
print (f'Average Change: ${ChngAvg}')
print (f'Greatest Increase in Profits: {DateMax} $({max(change)})') 
print (f'Greatest Decrease in Profits: {DateMin} $({min (change)})')
