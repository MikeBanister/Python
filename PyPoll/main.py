import os
import csv

#variables
data_path = "Resources/election_data.csv"
charles_count = 0
diana_count = 0
raymon_count = 0
total_count = 0

#Read csv
with open(data_path, encoding="utf-8") as data_file:
    reader = csv.reader(data_file, delimiter=",")

    #count loop
    for row in reader:

        if row[2] == "Charles Casper Stockham":
            charles_count = charles_count + 1

        elif row[2] == "Diana DeGette":
            diana_count = diana_count + 1

        elif  row[2] == "Raymon Anthony Doane":
            raymon_count = raymon_count + 1

    #calculate total        
    total_count = charles_count + diana_count + raymon_count

    #calculate percentages
    charles_percent = "{0:.3%}".format(charles_count / total_count)
    diana_percent = "{0:.3%}".format(diana_count / total_count)
    raymon_percent = "{0:.3%}".format(raymon_count / total_count)

    #calculate winner
    final_counts = {
        charles_count: "Charles Casper Stockham",
        diana_count: "Diana DeGette",
        raymon_count: "Raymon Anthony Doane"
        }
    winner = final_counts.get(max(final_counts))

    #compile results
    results_list = ([
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_count}",
        "-------------------------",
        f"Charles Casper Stockham: {charles_percent} ({charles_count})",
        f"Diana DeGette: {diana_percent} ({diana_count})",
        f"Raymon Anthony Doane: {raymon_percent} ({raymon_count})",
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------",
    ])

    #print to file
    with open("Results.txt","w") as result:
        result.writelines("\n".join(results_list))

    #print to terminal
    print("\n".join(results_list))