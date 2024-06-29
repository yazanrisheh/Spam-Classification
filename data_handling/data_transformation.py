from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

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
print("The tesing accuracy is ", test_accuracy * 100, "%")

# The training accuracy is  95.78095402100912 %
# The tesing accuracy is  94.17670682730925 %