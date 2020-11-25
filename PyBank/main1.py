# import the budget_data.csv file that only has 2 columns 'Date & Profit/Losses'
import os
import csv

csvpath_in = os.path.join("Resources", "budget_data.csv")
csvpath_out = os.path.join("Analysis", "pybank.txt")
#print(csvpath_in)

# MonthsTotal = 0
# NetTotal = 0
# CurrentBudget = 0
# PreviousBudget = 0
# ChangeTotal = 0
# GreatestIncrease = 0
# GreatestDecrease = 0
# GreatestIncreaseDate = ""
# GreatestDecreaseDate = ""

#open(cvspath) as csvfile:
with open(csvpath_in) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvfile.readline()
    print(csvreader)

    # rows = csv.reader(csvfile)
    # changeCount = 0
    # change = 0

    # for row in rows:
    #     MonthsTotal += 1
    #     CurrentBudget = int(row[1])
    #     NetTotal += CurrentBudget

    #     if PreviousBudget != 0:
    #         change = CurrentBudget - PreviousBudget
    #         ChangeTotal = change
    #         changeCount += 1
    #         print(change)

    #     PreviousBudget = CurrentBudget

    #     if change > GreatestIncrease:
    #         GreatestIncrease = change
    #         GreatestIncreaseDate = row(0)

    #     if change < GreatestDecrease:
    #         GreatestDecrease = change
    #         GreatestDecreaseDate = row(0)

    # print(f"ChangeCount: {ChangeCount}")
    # print(f"Total of Changes: {ChangeTotal}")

#print(MonthsTotal)
#print(NetTotal)
#print(GreatestIncreaseDate, GreatestIncrease)
#print(GreatestDecreaseDate, GreatestDecrease)

# output = f"""
# Financial Analysis
# ------------------------------------
# Total Months: {MonthsTotal}
# Total: {NetTotal:,}
# Average Change: ${ChangeTotal/ChangeCount:.2f}
# Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease:,})
# Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease:,})
"""

# print(output)

# with open(csvpath_out, 'w') as outputfile:
#     outputfile.write(output)

