import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Asus\Documents\Spam ML\data_handling\final_data.csv")

# Filter the dataframe with @ signs for any email in the dataset
df_cleaned = df[~df['sms'].str.contains('@')]

# Save the cleaned dataframe to a new CSV file
df_cleaned.to_csv('updated.csv', index=False)

print("File has been cleaned and saved.")
