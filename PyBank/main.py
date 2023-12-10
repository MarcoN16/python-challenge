# Financial Analysis
import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget_file = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(budget_file)
    total_month = 0
    total_value = 0
    previous_value = 0
    changing_max = 0
    changing_min = 0

    # Read each row of data after the header
    for row in budget_file:
        date_month = (row[0])
        value_month = int(row[1])
        total_month +=1
        total_value = total_value + value_month
        current_value = value_month

        if  previous_value == 0:
            total_changing = 0
            previous_value = current_value
        
        changing = current_value - previous_value  
        total_changing = total_changing + changing
        previous_value = current_value

        if changing > changing_max:
                changing_max = changing
                date_max = date_month
        
        elif changing < changing_min:
                changing_min = changing
                date_min = date_month

changing_average = round(total_changing / (total_month-1),2)

summary = (
    "\n"
    "Financial Analysis\n"
    "\n"
    "----------------------------\n"
    "\n"
    f"Total Months: {str(total_month)}\n"
    "\n"
    f"Total: ${str(total_value)}\n"
    "\n"
    f"Average Change: ${str(changing_average)}\n"
    "\n"
    f'Greatest Increase in Profits: {date_max} (${str(changing_max)})\n'
    "\n"
    f'Greatest Decrease in Profits: {date_min} (${str(changing_min)})\n'
    "\n"
)

print(summary)

output_file = 'Financial_Analysis.txt'
output_path = os.path.join("analysis", output_file)
with open(output_path, 'w') as outfile:
      outfile.write(summary)

print(f"Financial analysis has been exported to '{output_file}'")      

