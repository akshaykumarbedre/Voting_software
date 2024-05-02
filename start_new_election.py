import pandas as pd 
df=pd.read_csv("voter_ids.csv")
print(df)

import csv

def create_empty_csv(filename):
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)


        writer.writerow([])

# Usage
create_empty_csv('voting_data.csv')

