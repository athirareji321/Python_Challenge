# import the relavant modules
import os
import csv

# setting the terminal directory based on the current file path
current_file_path= os.path.abspath(__file__)
current_file_directory= os.path.dirname(current_file_path)
os.chdir(current_file_directory)

# create lists required to hold the data needed
months = []
profitloss_changes=[]

# defining initial variables
total_months=0
total_profitloss=0
profitloss_change=0
previous_profitloss=0
initial_profitloss=0

# defining the file path to read data
csvpath=os.path.join("pybankresources", "budget_data.csv")

# opening and reading the given data file
with open(csvpath, newline='') as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvfile)
    
    # read through all the rows and count the total no of months and the total profit loss
    for row in csvreader:

        total_months=total_months+1

        initial_profitloss= int(row[1])

        total_profitloss=total_profitloss+ initial_profitloss         
       
        if(total_months==1):

            previous_profitloss=initial_profitloss
            continue

        else:
            profitloss_change=initial_profitloss-previous_profitloss

            months.append(row[0])

            profitloss_changes.append(profitloss_change)

            previous_profitloss=initial_profitloss

    # calculating the average of profit loss change 
    sum_profitlosschange=sum(profitloss_changes)    
    avg_profitlosschange=round(sum_profitlosschange/(total_months-1), 3) 

# calculation the greatest increase and decrease with date and amount over the entire period
# firstly, calculating the max and min values
highest_value = max(profitloss_changes)
lowest_value = min(profitloss_changes)

# secondly, finding the index number for the months in which the values were highest and lowest
highest_value_month = profitloss_changes.index(highest_value)
lowest_value_month = profitloss_changes.index(lowest_value)

# thirdly, finding the months with the corresponding index values
highest_month= months[highest_value_month]
lowest_month = months[lowest_value_month]

# printing out the output to terminal
print("Financial Analysis")
print("--------------------------------------------------------------")
print(f"Total: {total_months} Months")
print(f"Total Profit/Loss: ${total_profitloss}")  
print(f'The Average Profit/Loss Change : ${avg_profitlosschange}')
print(f'Greatest Increase in Profits: {highest_month}, {highest_value}')
print(f'Greatest Decerease in Profits: {lowest_month}, {lowest_value}')

# printing the output to an external text file
file=os.path.join("pybankanalysis", "pybank_budget_data.txt")
with open(file, "w") as output_file:

    output_file.write("Financial Analysis\n")
    output_file.write("--------------------------------------------------------------\n")
    output_file.write(f"Total: {total_months} Months\n")
    output_file.write(f"Total Profit/Loss: ${total_profitloss}\n")  
    output_file.write(f'The Average Profit/Loss Change : ${avg_profitlosschange}\n')
    output_file.write(f'Greatest Increase in Profits: {highest_month}, {highest_value}\n')
    output_file.write(f'Greatest Decerease in Profits: {lowest_month}, {lowest_value}\n')




