#import dependencies
import os
import csv

Total = 0
Total_number_of_months = 0
Average_change_profit_loss = 0
Total_profit_loss_change = 0
previous_row = 0
current_row = 0
change = 0
List_of_Changes = []
greaterchange = 0
lesserchange = 0

#Open the csv file path
budget_data_path = os.path.join('.','Homework','Homework_#3', 'python_challenge','PyBank','budget_data.csv')

#Open the csv file
with open (budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile)

#Define the header
    budget_header = next(csvfile)

    for row in csv_reader:

        current_row = int(row[1])

        #Find the total # of months
        Total_number_of_months = Total_number_of_months + 1
        #Find the total amount
        Total = Total + current_row

            
        if previous_row != 0:
            change = current_row - previous_row
            List_of_Changes.append(change)
            Length_of_List = len(List_of_Changes)
            Total_profit_loss_change = Total_profit_loss_change + change
            Average_change_profit_loss = Total_profit_loss_change / Length_of_List

            if change > greaterchange:
                greaterchange = change
                max_change = max(List_of_Changes)
                max_change_date = row[0]

            if change < lesserchange:
                lesserchange = change
                min_change = min(List_of_Changes)
                min_change_date = row[0]  

        previous_row = current_row

output_path = os.path.join('.','Homework','Homework_#3', 'python_challenge','PyBank','Summary.txt')
with open(output_path,'w',newline='') as summarytext:
    text_writer = csv.writer(summarytext)
    text_writer.writerow(["Financial Analysis"])
    text_writer.writerow(["-----------------------------------"])
    text_writer.writerow([f"Total Months: {Total_number_of_months}"])
    text_writer.writerow([f"Total: ${Total}"])
    text_writer.writerow(["Average Change: " + "$" + str(round((Average_change_profit_loss),2))])
    text_writer.writerow([f"Greatest Increase in Profits: {max_change_date} (${max_change})"])
    text_writer.writerow([f"Greatest Decrease in Profits: {min_change_date} (${min_change})"])

print(f"Financial Analysis")
print(f"-----------------------------------")
print(f"Total Months: {Total_number_of_months}")
print(f"Total: ${Total}")
print("Average Change: " + "$" + str(round((Average_change_profit_loss),2)))
print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")

            
    