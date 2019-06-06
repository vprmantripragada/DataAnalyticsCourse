import csv
import os
# unique candidates list using a function call
#def unique (candidates):
   # unique_candidates = []
    #for candidate in candidates:
    #    if candidate not in unique_candidates:
     #       unique_candidates.append(candidate)
    #for u_candidate in unique_candidates:
     #   print (u_candidate)


data_path = os.path.join('Resources', 'election_data.csv')
with open(data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    voter_count = 0
    candidates = []
    unique_candidates = []

    for row in csvreader:
        # count the total number of voters
        voter_count += 1
        #create a list containing all the rows in column C of the excel file 
        candidates.append(row[2])
    # print total voters
    print("Total voters: " + str(voter_count))

    # create the unique list of candidates        
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    for u_candidate in unique_candidates:
        print (u_candidate)
   
    votes_uc0 = 0
    votes_uc1 = 0
    votes_uc2 = 0
    votes_uc3 = 0
   # to count votes for individual uniaaue voters
    for candidate in candidates:
        if candidate == unique_candidates[0]:
            votes_uc0 += 1
        if candidate == unique_candidates[1]:
            votes_uc1 += 1
        if candidate == unique_candidates[2]:
            votes_uc2 +=1
        if candidate == unique_candidates[3]:
            votes_uc3 += 1
    print("total votes for " + unique_candidates[0] + " are " + str(votes_uc0))
    print("total votes for " + unique_candidates[1] + " are " + str(votes_uc1))
    print("total votes for " + unique_candidates[2] + " are " + str(votes_uc2))
    print("total votes for " + unique_candidates[3] + " are " + str(votes_uc3))

    uc_votes = [votes_uc0,votes_uc1, votes_uc2, votes_uc3]
    
    percent = []
    
    for x in range(len(uc_votes)):
        percent.append(round(uc_votes[x]/voter_count*100, 2))
    print("percents: " + str(percent))

    #percent_uc0 = round(votes_uc0/voter_count*100, 2)
    #percent_uc1 = round(votes_uc1/voter_count*100, 2)
    #percent_uc2 = round(votes_uc2voter_count*100, 2)
    #percent_uc3 = round(votes_uc3voter_count*100, 2)

    #percent = [percent_uc0, percent_uc1, percent_uc2, percent_uc3]

    table = zip(unique_candidates, uc_votes, percent)
    print(table)
    winner = 0 
    for x in range(len(percent)):
        if percent [x] > winner:
            winner = percent [x]
            winner_name = unique_candidates [x]
    print("The winner candidate is " + winner_name + " who won by " + str(winner) + " % votes")





        
    

    

    