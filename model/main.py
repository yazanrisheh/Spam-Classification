import pickle

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#  remove stopwords from count, do not accept any links except from mawad.ae, links can be with .jpg or so

class MessageRequest(BaseModel):
    message: str

@app.post("/predict")
async def predict(request: MessageRequest):
    # Load the saved model and count vectorizer
    model = pickle.load(open(r"C:\Users\Asus\Documents\Spam ML\pickle_dir\spam_model.pkl", "rb"))
    cv = pickle.load(open(r"C:\Users\Asus\Documents\Spam ML\pickle_dir\count_vectorizer.pkl", "rb"))

    message_count = cv.transform([request.message])
    pred = model.predict(message_count)
    prediction = "Spam" if pred[0] == 1 else "Not Spam"

    return {"prediction": prediction}
