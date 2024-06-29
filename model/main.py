import pickle

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = pickle.load(open(r"C:\Users\Asus\Documents\Spam ML\pickle_dirspam_model.pkl", "rb"))
cv = pickle.load(open(r"C:\Users\Asus\Documents\Spam ML\pickle_dircount_vectorizer.pkl", "rb"))

class MessageRequest(BaseModel):
    message: str

@app.post("/predict")
async def predict(request: MessageRequest):
    
    message_count = cv.transform([request.message])
    pred = model.predict(message_count)
    prediction = "Spam" if pred[0] == 1 else "Not Spam"

    return {"prediction": prediction}
