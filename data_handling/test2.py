from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import os
import unicodedata

df = pd.read_csv(r"C:\Users\Asus\Documents\Spam ML\data_handling\further_filtered_data.csv")

# Split the balanced data for training
x_train, x_test, y_train, y_test = train_test_split(df.sms, df.label, test_size=0.3)

cv = CountVectorizer()
x_train_count = cv.fit_transform(x_train)
model = MultinomialNB()
model.fit(x_train_count, y_train)

# Calculate accuracy on training data
train_predictions = model.predict(cv.transform(x_train))
train_accuracy = accuracy_score(y_train, train_predictions)
print("The training accuracy is ", train_accuracy * 100, "%")

# Calculate accuracy on testing data
test_predictions = model.predict(cv.transform(x_test))
test_accuracy = accuracy_score(y_test, test_predictions)
print("The testing accuracy is ", test_accuracy * 100, "%")

# Find incorrectly classified examples
incorrect_indices = []
for i, (pred, true) in enumerate(zip(test_predictions, y_test)):
    if pred != true:
        incorrect_indices.append(i)

# Print the number of incorrectly classified examples
print("\nNumber of incorrectly classified examples:", len(incorrect_indices))

# Determine the filename based on existing files
file_number = 1
while os.path.exists(f"incorrect_{file_number}.csv"):
    file_number += 1

filename = f"incorrect_{file_number}.csv"

# Print the incorrectly classified SMS messages and their actual labels
print("\nIncorrectly classified SMS messages:")
print()

# Create or append to the file, handling Unicode
with open(filename, 'a' if os.path.exists(filename) else 'w', encoding='utf-8') as f:
    f.write("SMS,Predicted,Actual\n")
    for i in incorrect_indices:
        sms = x_test.iloc[i]
        # Replace problematic characters with their ASCII equivalents (if available)
        for char in sms:
            if ord(char) > 127:
                replacement = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
                sms = sms.replace(char, replacement)
        f.write(f"{sms},{test_predictions[i]},{y_test.iloc[i]}\n")

# Check if 10 files exist and create "incorrect_final" if so
if file_number >= 10:
    all_incorrect_messages = []
    for i in range(1, 11):
        with open(f"incorrect_{i}.csv", 'r', encoding='utf-8') as f:
            lines = f.readlines()[1:]  # Skip header
            all_incorrect_messages.extend(lines)

    with open("incorrect_final.csv", 'w', encoding='utf-8') as f:
        f.write("SMS,Predicted,Actual\n")
        f.writelines(all_incorrect_messages)