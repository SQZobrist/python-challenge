import os
import csv
import sys


totalV = 0
candidates = {}
candNames = []
winner = ["", 0, 0]
voteSet = []
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
percent = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for data in csvreader:
        voteSet.append(data[2])
        candidates[data[2]] = 1
    
for votes in voteSet:
    candidates[votes] += 1
            
    
    
totalV = len(voteSet)

print("Results: Total Votes: ", totalV, "  ") 

candNames = list(candidates.keys())
for cand in candNames:
    
    percent = round(((candidates[cand] / totalV) * 100), 4)
    
    print(cand, ": ", percent, "% (", candidates[cand], ")  " )
    
    if winner[1] < candidates[cand]:
        winner[1] = candidates[cand]
        winner[2] = percent
        winner[0] = cand
            
print("  And the winner is: ", winner[0])

with open('Output.txt', newline="") as csvfile:
    sys.stdout = open('Output.txt', 'w')

    print("Results: Total Votes: ", totalV, "  ") 

    candNames = list(candidates.keys())
    for cand in candNames:
    
        percent = round(((candidates[cand] / totalV) * 100), 4)
    
        print(cand, ": ", percent, "% (", candidates[cand], ")  " )
    
        if winner[1] < candidates[cand]:
            winner[1] = candidates[cand]
            winner[2] = percent
            winner[0] = cand
            
     print("  And the winner is: ", winner[0])
