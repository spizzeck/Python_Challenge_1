#Main script that will be run
import os
import csv
import statistics

#Files to load and write as text
file_load=os.path.join("Resources", "budget_data.csv")
file_to_text=os.path.join("Analysis", "budget_analysis.txt")
#Track various parameters
total_months=0
month_change=[]
change_list=[]
greatest_increase=["", 0]
greatest_decrease=["", 999999999999999]
total_profits=0

#Read csv file and convert to list of dicts
with open(file_load) as budget_data:
    reader=csv.reader(budget_data)

    #Read header row
    header=next(reader)

    #Remove first row to avoid appending to change_list
    first_row=next(reader)
    total_months+=1
    total_profits+=int(first_row[1])
    prev_profit=int(first_row[1])

    for row in reader:
        #Track thte total
        total_months+=1
        total_profits+=int(row[1])

        #Track the net change
        net_change=int(row[1])-prev_profit
        prev_profit=int(row[1])
        change_list+=[net_change]
        month_change+=[row[0]]

        #Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change

        #Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change

#Calculate the Average Change
avg_monthly_change=sum(change_list) / len(change_list)

#Generate the Analysis Summary
analysis= (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profits}\n"
    f"Average Change: ${avg_monthly_change:.1f}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decerease: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
#Print the analysis to terminal
print(analysis)

#Export to text file
with open(file_to_text, "w") as txt_file:
    txt_file.write(analysis)