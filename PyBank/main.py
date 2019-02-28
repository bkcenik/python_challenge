import os
import csv

filepath = os.path.join("Resources","budget_data.csv") #sets filepath

with open(filepath, newline ="") as csvfile: #read in csvfile
    csvreader = csv.reader(csvfile, delimiter =",")
    head = next(csvreader) #skip header

    # make empty lists
    months = []
    profit_loss = []
    profit_loss_change = []

    print("Financial analysis: \n----------------------------")
    
    for row in csvreader: #calculate total months and total revenue
        months.append(row[0])
        totalmonth = len(months)
        profit_loss.append(int(row[1]))
        totalprofit = sum(profit_loss)
    print(f"Total months: {totalmonth} \nTotal: ${totalprofit}")
    
    for x in range(1, totalmonth): #calculate revenue change
        profit_loss_change.append(profit_loss[x] - profit_loss[x-1])
        average_change = round((sum(profit_loss_change) / len(profit_loss_change)),2)
    print(f"Average Change: ${average_change}")

    # calculate greatest increase and decrease, and corresponding months
    greatest_increase = max(profit_loss_change)
    greatest_decrease = min(profit_loss_change)
    increase_month = months[profit_loss_change.index(greatest_increase) + 1]
    decrease_month = months[profit_loss_change.index(greatest_decrease) + 1]
    print(f"Greatest increase in profits: {increase_month} (${greatest_increase})")
    print(f"Greatest decrease in profits: {decrease_month} (${greatest_decrease})")


    outputpath = ("output.txt") # path to output file

    with open(outputpath, "w", newline="") as text: #initialize text writer
        line1 = text.write("Financial analysis:\n")
        line2 = text.write("----------------------------\n")
        line3 = text.write(f"Total months: {totalmonth}\n")
        line4 = text.write(f"Total: ${totalprofit}\n")
        line5 = text.write(f"Average Change: ${average_change}\n")
        line6 = text.write(f"Greatest increase in profits: {increase_month} (${greatest_increase})\n")
        line7 = text.write(f"Greatest decrease in profits: {decrease_month} (${greatest_decrease})")
 