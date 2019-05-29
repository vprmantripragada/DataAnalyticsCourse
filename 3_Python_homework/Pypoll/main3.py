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
    # for u_candidate in unique_candidates:
    #    print (u_candidate)    
         
    votes=[0,0,0,0]
   # to count votes for individual unique voters
    for x in range(len(unique_candidates)):
        for candidate in candidates:
            if candidate == unique_candidates[x]:
                votes[x] += 1
   # print ("total votes for each candidate are " + str(votes))
    
    percent = []
    for x in range(len(votes)):
        percent.append(round(votes[x]/voter_count*100, 2))
    # print("percents: " + str(percent))

    for x in range(len(unique_candidates)):
        print ("candidate: " + unique_candidates[x] + " percent_votes: " + str(percent[x]) + " vote_count: " + str(votes[x]))
    
    winner = 0 
    for x in range(len(percent)):
        if percent [x] > winner:
            winner = percent [x]
            winner_name = unique_candidates [x]
    print("The winner candidate is " + winner_name + " who won by " + str(winner) + " % votes")

results = zip(unique_candidates, percent, votes)
results_path = os.path.join("results.txt")

with open(results_path, 'w', newline='') as txtfile:
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(['Candidate', 'Votes', 'Percent'])
    txtwriter.writerow(results)
    txtwriter.writerow(['The winner candidate is ' + winner_name])

   






        
    

    

    