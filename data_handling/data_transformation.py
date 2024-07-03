import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

def load_and_train_data(file_path):
    df = pd.read_csv(file_path)
    x_train, x_test, y_train, y_test = train_test_split(df['sms'], df['label'], test_size=0.25)
    cv = CountVectorizer()
    x_train_count = cv.fit_transform(x_train)
    x_test_count = cv.transform(x_test)
    model = MultinomialNB()
    model.fit(x_train_count, y_train)
    # Calculate training accuracy
    train_accuracy = accuracy_score(y_train, model.predict(x_train_count))
    return model, cv, x_train_count, y_train, x_test_count, y_test, train_accuracy

def save_incorrect_data(df, predictions, y_test, filename):
    incorrect_indices = [i for i, (pred, true) in enumerate(zip(predictions, y_test)) if pred != true]
    incorrect_df = df.iloc[incorrect_indices].copy()
    incorrect_df['predicted'] = [predictions[i] for i in incorrect_indices]
    incorrect_df.to_csv(filename, index=False)
    return len(incorrect_indices)  # Return the count of incorrect classifications

def save_model_and_vectorizer(model, vectorizer, directory):
    model_path = f'{directory}\\spam_model.joblib'
    vectorizer_path = f'{directory}\\count_vectorizer.joblib'
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    print(f"Model and vectorizer saved in {directory}")

def main():
    file_path = r"C:\Users\Asus\Documents\Spam ML\data_handling\final_data.csv"
    directory = r"C:\Users\Asus\Documents\Spam ML\joblib_dir"
    model, cv, x_train_count, y_train, x_test_count, y_test, train_accuracy = load_and_train_data(file_path)
    save_model_and_vectorizer(model, cv, directory)
    test_predictions = model.predict(x_test_count)
    test_accuracy = accuracy_score(y_test, test_predictions) * 100
    
    print(f"The training accuracy is {train_accuracy * 100:.2f}%")
    print(f"The testing accuracy is {test_accuracy:.2f}%")
    
    df_test = pd.read_csv(file_path).iloc[y_test.index]  # Correctly slice the test portion
    num_incorrect = save_incorrect_data(df_test, test_predictions, y_test, "incorrect_examples.csv")
    
    print("\nNumber of incorrectly classified examples:", num_incorrect)
    print("Incorrectly classified SMS messages saved to: incorrect_examples.csv")

if __name__ == "__main__":
    main()

