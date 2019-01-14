import os
import csv
import sys


totalV = 0
candidates = []
winner = ["", 0, 0]

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for data in csvreader:
        totalV += 1
        
        testC = 0
        
        for cand in candidates:
            if cand == data[2]:
                testC += 1
                cand[1] += 1
                
        if testC == 0:
            candidates.append([data[2], 1, 0])
    
    
    print("Results: Total Votes: ", totalV, "  ")    
    
    for cand in candidates:
        cand[2] = (cand[1] / totalV) * 100
        print(cand[0], ": ", cand[2], "% (", cand[1], ")  " )
        if winner[1] < cand[1]:
            winner = cand
            
    print("  And the winner is: ", winner[0])
    
 with open('Output.txt', newline="") as csvfile:
    sys.stdout = open('Output.txt', 'w')
    print("Results: Total Votes: ", totalV, "  ") 
    for cand in candidates:
        cand[2] = (cand[1] / totalV) * 100
        print(cand[0], ": ", cand[2], "% (", cand[1], ")  " )
        if winner[1] < cand[1]:
            winner = cand
            
    print("  And the winner is: ", winner[0])
