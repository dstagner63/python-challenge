import os
import csv
import pandas as pd

csvpath_in = os.path.join("Resources", "budget_data.csv")
csvpath_out = os.path.join("Analysis", "pybank.txt")
print(csvpath_in)

df = pd.read_csv(csvpath_in)
df.head()

total_months = len(df['Date'].unique())
str_total_months = 'Total Months: ' + str(total_months)
# str_total_months

net_total = df['Profit/Losses'].sum()
str_net_total = 'Total: $'+ str(net_total)
# str_net_total

change_list = []
sum_change = 0

for row in df.index[:-1]:
    current_row = df['Profit/Losses'][row]
    next_row = df['Profit/Losses'][row+1]
    change = next_row - current_row
    # Store each change in a list 
    change_list.append(change)
    # Add each change to sum of previous changes
    sum_change = sum_change + change 

average_change = sum_change / len(change_list)
average_change = "{:.2f}".format(average_change)
str_average_change = 'Average Change: $' + str(average_change)
# str_average_change

greatest_increase = max(change_list)
greatest_decrease = min(change_list)

index_max = change_list.index(greatest_increase)
index_min = change_list.index(greatest_decrease)

date_max = df['Date'][index_max +1]
date_min = df['Date'][index_min +1]

str_greatest_increase = 'Greatest Increase in Profits: %s ($%d)' %(date_max, greatest_increase)

str_greatest_decrease = 'Greatest Decrease in Profits: %s ($%d)' %(date_min, greatest_decrease)

print('Financial Analysis')
line_seperator = '--------------------------'
print(line_seperator)
print(str_total_months)
print(str_net_total)
print(str_average_change)
print(str_greatest_increase)
print(str_greatest_decrease)
print(line_seperator)

file = open(csvpath_out, 'w')
file.write('Financial Analysis\n')
file.write('--------------------------\n')
file.write(str_total_months)
file.write('\n')
file.write(str_net_total)
file.write('\n')
file.write(str_average_change)
file.write('\n')
file.write(str_greatest_increase)
file.write('\n')
file.write(str_greatest_decrease)
file.write('\n')
file.write('--------------------------')
file.close()