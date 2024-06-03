import pandas as pd


df = pd.read_csv(r"C:\Users\Asus\Documents\Spam ML\data_handling\cleaned_data.csv")

# # Check for any missing values
# x = df.isnull().sum()
# print(x)


df['sms'] = df['sms'].str.lower()

# y = df['label'].value_counts()
# print(y)

# 0    4827
# 1    3500
# Name: count, dtype: int64

# shuffled_df = df.sample(frac=1).reset_index(drop=True)

# # Save the shuffled data back to cleaned_data.csv
# shuffled_df.to_csv("cleaned_data.csv", index=False)
