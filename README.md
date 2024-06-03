# Spam Classification API

https://www.kaggle.com/code/satyajeet007/nb-amazon-reviews-satyajeet
Dataset to test out

This project implements a simple FastAPI-based API for spam classification using a Naive Bayes classifier trained on a dataset of SMS messages. It allows users to submit a message and receive a prediction indicating whether the message is spam or not.

## Getting Started

To run the API locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yazanrisheh/Spam-Classification.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8888                               
   ```

The API will be accessible at `http://localhost:8000`.

## Usage

### Predict

Endpoint: `/predict`

#### Request

- Method: `POST`
- Body:
  ```json
  {
    "message": "Your message here."
  }
  ```

#### Response

```json
{
  "prediction": "Spam"
}
```

### Training Data

The model is trained on all the csv files dataset provided in the repository in the data directory. It consists of  messages labeled as 1 or 0.

## Model Training

The model is trained using the Multinomial Naive Bayes algorithm with Count Vectorization of text data.

## Additional Information

- `spam_model.pkl`: Pickled file containing the trained Naive Bayes model.
- `count_vectorizer.pkl`: Pickled file containing the Count Vectorizer used for feature extraction.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

