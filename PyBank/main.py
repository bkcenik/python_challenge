import os
import csv

budgetpath = os.path.join('Resources', 'budget_data.csv')

with open(budgetpath, newline='') as csvfile:
    print(csvfile) #tocheckpath
    budgetreader = csv.reader(csvfile, delimiter=',') #read in file
    budget_header = next(budgetreader) #skip header
    print(f"Header: {budget_header}") #print the header to confirm

    #create lists for total month, revenue(profit/loss), revenue change
    months = []
    revenue = []
    revenue_change = []

    print("Financial Analysis:")
    print("------------------------------------------------------------")

    for row in budgetreader:
        months.append(row[0])
        totalmonth = len(months) #calculates number of months
        revenue.append(int(row[1]))
        totalrevenue = sum(revenue) #calculates total revenue
    print(f"Total Months: {totalmonth}. \nTotal revenue: {totalrevenue}") #print output
    
    for x in range(1, totalmonth):
        revenue_change.append(revenue[x] - revenue[x-1]) 
        #calculate revenue change
        #by subtracting each row from the previous
        average_change = (sum(revenue_change)/len(revenue_change))
    print(f"Average change was ${average_change}.")

    # define greatest profit and loss
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
    increase_month = months[revenue_change.index(greatest_increase) + 1]
    decrease_month = months[revenue_change.index(greatest_decrease) + 1]
    print(f"Greatest increase was {greatest_increase}, in {increase_month}")
    print(f"Greatest decrease was {greatest_decrease}, in {decrease_month}")

#create the output file:
#with open("output.txt", "w") as txtfile:

