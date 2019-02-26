import os
import csv

electionfile = os.path.join("resources", "election_data.csv")

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

with open(electionfile, newline='') as csvfile:
    print(csvfile) #tocheckpath
    electionreader = csv.reader(csvfile, delimiter=',') #read in file
    election_header = next(electionreader) #skip header
    print(f"Header: {election_header}") #print the header to confirm

    votes_cast = []
    candidate_list = []
    total_votes = []
    splitter = ("----------------------------------------------------------")

    print("Election results:")
    print(splitter)
    for row in electionreader :
        votes_cast.append(row[2])
        votecount = len(votes_cast)
    
    print(f"Total number of votes: {votecount}")
    print(splitter)


