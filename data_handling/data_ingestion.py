import pandas as pd


df = pd.read_csv(r"C:\Users\Asus\Documents\Spam ML\data_handling\final_data.csv", encoding='ISO-8859-1')

# # Check for any missing values
# x = df.isnull().sum()
# print(x)


df['sms'] = df['sms'].str.lower()

# y = df['label'].value_counts()
# print(y)

# 0    4274
# 1    3947
# Name: count, dtype: int64

shuffled_df = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled data back to cleaned_data.csv
shuffled_df.to_csv("final_data.csv", index=False)


# joblib data
# The training accuracy is 96.26%
# The testing accuracy is 94.87%

# Number of incorrectly classified examples: 106
# Incorrectly classified SMS messages saved to: incorrect_examples.csv
