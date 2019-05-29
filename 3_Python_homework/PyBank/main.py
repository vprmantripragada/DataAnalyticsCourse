import csv
import os


data_path = os.path.join('Resources', 'budget_data.csv')
with open(data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months_count = 0
    net_amount = 0
    max_inc = 0
    max_dec = 0
    for row in csvreader:
        months_count += 1
        net_amount += float(row[1])
       # max_inc = max(row[1])
       # max_dec = min(row[1])
        if float(row[1])> max_inc:
            max_inc = float(row[1])
            max_month = row[0]
        if float(row[1])< max_dec:
            max_dec = float(row[1])
            min_month = row[0]     
    print("Total months included in the dataset are " + str(months_count))
    print("Net total profit/loss over the entire period is " + str(net_amount))
    average_amount = net_amount/months_count
    print("The average changes in profit/loss over the entire period is " + str(average_amount))
    print("The max increase in profits was in " + max_month + " " + str(max_inc))
    print("The max decrease in profits was in " + min_month + " " + str(max_dec))

export_path = os.path.join('results.txt')
with open (export_path, 'w') as txtfile: 
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(["Total months included in the dataset are " + str(months_count)])
    txtwriter.writerow(["Net total profit/loss over the entire period is " + str(net_amount)])
    txtwriter.writerow(["The average changes in profit/loss over the entire period is " + str(average_amount)])
    txtwriter.writerow(["The max increase in profits was in " + max_month + str(max_inc)])
    txtwriter.writerow(["The max decrease in profits was in " + min_month + str(max_dec)])








