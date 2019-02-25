import os
import csv

electionfile = os.path.join("resources", "election_data.csv")



with open(electionfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    vote = []
    candidate_list = []
    candidate_vote = []

    for row in csvreader:
        vote.append(csvreader[0])
        totalvote = len(vote)
        print(totalvote)

