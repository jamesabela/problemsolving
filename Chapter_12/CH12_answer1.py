# Create dictionary tracking match data  
standings = {  
    "Team Alpha": [12, 4, 2], # Won, Drawn, Lost arrays  
    "Team Beta":  [10, 6, 2],  
    "Team Gamma": [8,  3, 7]  
}

with open("sports_standings.tsv", "w") as file:  
    # Explicitly separate column identifiers using tab characters  
    file.write("Team Name	Wins	Draws	Losses
")  
    for team, stats in standings.items():  
        file.write(f"{team}	{stats[0]}	{stats[1]}	{stats[2]}
")  
          
print("sports_standings.tsv written cleanly.")
