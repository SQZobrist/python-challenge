import os
import csv
import sys

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    
    lastMonth = 0
    monthCount = 0
    highestChange = 0
    lowestChange = 0
    netProfit = 0
    totalChange = 0
    
    for data in csvreader:
        thisMonth = int(data[1])
        
        monthCount = monthCount + 1
        
        netProfit = netProfit + int(data[1])
        
        change = thisMonth - lastMonth
        
        totalChange = totalChange + change
        
        if highestChange < change:
            highestChange = change
            highMonth = data[0]
            
        if lowestChange > change:
            lowestChange = change
            lowMonth = data[0]
            
        lastMonth = int(data[1])
    averageChange = totalChange / monthCount

    print("The total number of months:", monthCount)
    print("The total net amount of Profit/Losses:", netProfit)
    print("The average change in Profit/Losses:", averageChange)
    print("The greatest increase:", highestChange, " on ", highMonth)
    print("The greatest decrease:", lowestChange, " on ", lowMonth)
   
with open('Output.txt', newline="") as csvfile:
    sys.stdout = open('Output.txt', 'w')
    print("The total number of months:", monthCount)
    print("The total net amount of Profit/Losses:", netProfit)
    print("The average change in Profit/Losses:", averageChange)
    print("The greatest increase:", highestChange, " on ", highMonth)
    print("The greatest decrease:", lowestChange, " on ", lowMonth)
