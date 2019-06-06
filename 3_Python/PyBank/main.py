import csv
import os

amounts = []
months = []
net_amount = 0
difference = []
max_inc = 0
max_dec = 0

data_path = os.path.join('Resources', 'budget_data.csv')
with open(data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        amounts.append(row[1])
        months.append(row[0])
        net_amount += float(row[1])
    total_months = len(amounts)
    print ("Total Months: " + str(total_months))
    print ("Net Amount: $" + str(net_amount))
    start_amount = float(amounts[0])
    end_amount = float (amounts [total_months-1])
    average_change = round((end_amount - start_amount)/(total_months - 1), 2)
    print ("Average  Change: $" + str(average_change))

    for i in range (len(amounts)):
        diff = (float(amounts[i])-float(amounts[i-1]))
        difference.append(diff)
    #for i in range (len(difference)):   
        if float(difference[i])> max_inc:
            max_inc = difference[i]
            max_month = months[i]
        if float(difference[i])< max_dec:
            max_dec = difference[i]
            min_month = months[i]
    print("The max increase in profits was in " + max_month + " $" + str(max_inc))
    print("The max decrease in profits was in " + min_month + " $" + str(max_dec))


export_path = os.path.join('results.txt')
with open (export_path, 'w') as txtfile: 
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(["Total months included in the dataset are " + str(total_months)])
    txtwriter.writerow(["Net total profit/loss over the entire period is " + str(net_amount)])
    txtwriter.writerow(["The average changes in profit/loss over the entire period is " + str(average_change)])
    txtwriter.writerow(["The max increase in profits was in " + max_month + ", $" + str(max_inc)])
    txtwriter.writerow(["The max decrease in profits was in " + min_month + ", $" + str(max_dec)])

