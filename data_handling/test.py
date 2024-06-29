from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import os

df = pd.read_csv(r"C:\Users\Asus\Documents\Spam ML\data_handling\further_filtered_data.csv")

def load_and_train_data(file_path):
    df = pd.read_csv(file_path)
    x_train, x_test, y_train, y_test = train_test_split(df.sms, df.label, test_size=0.3)
    cv = CountVectorizer()
    x_train_count = cv.fit_transform(x_train)
    x_test_count = cv.transform(x_test)
    model = MultinomialNB()
    model.fit(x_train_count, y_train)
    train_accuracy = accuracy_score(y_train, model.predict(cv.transform(x_train)))
    test_accuracy = accuracy_score(y_test, model.predict(x_test_count))
    return train_accuracy, test_accuracy, model, cv

def find_incorrectly_classified_examples(test_predictions, y_test):
    incorrect_indices = []
    for i, (pred, true) in enumerate(zip(test_predictions, y_test)):
        if pred != true:
            incorrect_indices.append(i)
    return incorrect_indices

def write_incorrectly_classified_examples(df, incorrect_indices, filename):
    incorrect_df = df.iloc[incorrect_indices][['sms', 'label']].copy()
    incorrect_df.columns = ['sms', 'actual']
    incorrect_df['predicted'] = df.iloc[incorrect_indices]['label'].apply(lambda x: 0 if x == 0 else 1)
    incorrect_df.to_csv(filename, index=False)

def main():
    file_path = r"C:\Users\Asus\Documents\Spam ML\data_handling\further_filtered_data.csv"
    train_accuracy, test_accuracy, model, cv = load_and_train_data(file_path)
    print("The training accuracy is ", train_accuracy * 100, "%")
    print("The testing accuracy is ", test_accuracy * 100, "%")
    test_predictions = model.predict(cv.transform(df.sms))
    incorrect_indices = find_incorrectly_classified_examples(test_predictions, df.label)
    print("\nNumber of incorrectly classified examples:", len(incorrect_indices))
    file_number = 1
    while os.path.exists(f"incorrect_{file_number}.csv"):
        file_number += 1
    filename = f"incorrect_{file_number}.csv"
    write_incorrectly_classified_examples(df, incorrect_indices, filename)
    print("\nIncorrectly classified SMS messages:")
    print()

if __name__ == "__main__":
    main()