import os
import csv

electionfile = os.path.join("resources", "election_data.csv")

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

with open(electionfile, newline='') as csvfile:
    #print(csvfile) #to check path
    electionreader = csv.reader(csvfile, delimiter=',') #read in the csv file
    election_header = next(electionreader) #skip header
    #print(f"Header: {election_header}") #print the header to confirm

    # make empty lists
    votes_cast = [] #this will be used to count the total votes
    candidate_list = [] #this will be used to make a list of the 4 candidates
    candidate_votes = [] #this will be used to count the votes for each candidate
    splitter = ("----------------------------------------------------------")

    print("Election results:")
    print(splitter)
    for row in electionreader :
        votes_cast.append(row[2]) #add 3rd column to vote count
        votecount = len(votes_cast) # define vote count as the number of items in votes_cast
        if row[2] not in candidate_list : #add names of candidates
            candidate_list.append(row[2])
    # print(candidate_list) #test
    
    print(f"Total number of votes: {votecount}")
    print(splitter)

    for candidate in candidate_list: 
        candidate_votes.append(votes_cast.count(candidate)) #count votes cast for each candidate
    # print(candidate_votes) #test
    for x in range(len(candidate_list)): #loop through list of candidates
        percent_won = round(int(candidate_votes[x])/votecount * 100, 3)
        print(f"{candidate_list[x]}: {percent_won}% ({candidate_votes[x]})")
    print(splitter)
    
    winner = candidate_list[candidate_votes.index(max(candidate_votes))]
    print(f"Winner: {winner}")
    print(splitter)
