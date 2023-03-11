import os
import csv

#variables
data_path = "Resources/budget_data.csv"
months = 0
total_pl = 0
greatest_increase = 0
greatest_decrease = 0

#open csv
with open(data_path, encoding="utf-8") as data_file:
    reader = csv.reader(data_file, delimiter=",")
    next(reader)

    #read loop
    for row in reader:
        line_num = int(row[1])
        total_pl = total_pl + line_num
        months = months + 1

        #find greatest increase and date
        if line_num > greatest_increase:
            greatest_increase = line_num
            increase_date = row[0]

        #find greatest decrease and date
        if line_num < greatest_decrease:
            greatest_decrease = line_num
            decrease_date = row[0]
    
    #compile results
    results_list = (["Financial Analysis",
                    "----------------------------",
                    f"Total Months: {months}",
                    f"Total: ${total_pl}",
                    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})",
                    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})",
                    ])

    #print to file        
    with open("Results.txt","w") as result:
        result.writelines("\n".join(results_list))

    #print to terminal
    print("\n".join(results_list))


