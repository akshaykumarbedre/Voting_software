import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
# Initialize the data storage
columns = ['Voter_ID', 'Vote']
data = []
votes_df = pd.DataFrame(data, columns=columns)

# Function to check if the voter ID is valid
def is_valid_voter(voter_id):
    try:
        # Read the existing voter IDs from the CSV file
        existing_voters_df = pd.read_csv('voter_ids.csv')
        # Check if the voter ID exists in the DataFrame
        return voter_id in existing_voters_df['Voter_ID'].values
    except FileNotFoundError:
        # If the file does not exist, no voter IDs are registered yet
        return False

# Function to register the vote
def register_vote(voter_id, vote):
    global votes_df
    new_row = pd.DataFrame({'Voter_ID': [voter_id], 'Vote': [vote]})
    votes_df = pd.concat([votes_df, new_row], ignore_index=True)

# Function to submit the vote
def submit_vote():
    voter_id = voter_id_entry.get()
    vote = vote_var.get()
    if is_valid_voter(voter_id):
        # Check if the voter has already voted
        if voter_id not in votes_df['Voter_ID'].values:
            register_vote(voter_id, vote)
            voter_id_entry.delete(0, tk.END)
            result_label.config(text=f"Thank you for voting! Total votes: {len(votes_df)}")
            # Save to CSV after each vote
            save_to_csv()
        else:
            messagebox.showerror("Already Voted", "You have already cast your vote.")
    else:
        messagebox.showerror("Invalid Voter", "You are not registered to vote.")

# Function to save DataFrame to CSV
def save_to_csv():
    votes_df.to_csv('voting_data.csv', index=False)

# Function to display the results
def view_results():
    result_message = ""
    for candidate in votes_df['Vote'].unique():
        votes_count = votes_df[votes_df['Vote'] == candidate].shape[0]
        result_message += f"Candidate {candidate}: {votes_count} votes\n"
    messagebox.showinfo("Voting Results", result_message)

root = tk.Tk()
root.title("Online Voting System")
root.geometry("300x300") 

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), background='blue')
style.configure('TLabel', font=('Helvetica', 12), background='white')

main_frame = ttk.Frame(root, padding="30")
main_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(main_frame, text="Voter ID:",padx=20, pady=20).grid(row=0, column=0, sticky=tk.W)
voter_id_entry = ttk.Entry(main_frame)
voter_id_entry.grid(row=0, column=1, sticky=tk.EW)

vote_var = tk.StringVar()
ttk.Radiobutton(main_frame, text="Candidate A", variable=vote_var, value="A").grid(row=1, column=0, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Candidate B", variable=vote_var, value="B").grid(row=1, column=1, sticky=tk.W)

submit_button = ttk.Button(main_frame, text="Submit Vote", command=submit_vote)
submit_button.grid(row=2, column=0, columnspan=2, pady=5)

result_button = ttk.Button(main_frame, text="View Results", command=view_results)
result_button.grid(row=3, column=0, columnspan=2, pady=5)

result_label = ttk.Label(main_frame, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Make the grid columns expand equally
main_frame.columnconfigure(1, weight=1)

# Start the main loop
root.mainloop()