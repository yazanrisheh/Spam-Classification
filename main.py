from fastapi import FastAPI
from pydantic import BaseModel
from data_handling.pre_filter import validate_input_pre_model
from logs.log_config import logger  # Import the configured logger from your log_config module
import joblib
import time

app = FastAPI()

directory = r"C:\Users\Asus\Documents\Spam ML\joblib_dir"
model = joblib.load(f'{directory}\\spam_model.joblib')
cv = joblib.load(f'{directory}\\count_vectorizer.joblib')

class MessageRequest(BaseModel):
    message: str

@app.post("/predict")
async def predict(request: MessageRequest):
    start_time = time.time()

    # First validate the input for URLs and emails
    is_valid = validate_input_pre_model(request.message)

    # If invalid, classify as "Spam" and return immediately
    if not is_valid:
        end_time = time.time()
        response_time = end_time - start_time
        logger.info(f"Filtered by validate_input_pre_model: Spam | Processing time: {response_time:.3f} seconds")
        return {"prediction": "Spam", "response_time": f"{response_time:.3f} seconds"}

    # If valid, process with the model
    message_count = cv.transform([request.message])
    pred = model.predict(message_count)
    prediction = "Spam" if pred[0] == 1 else "Not Spam"
    end_time = time.time()
    response_time = end_time - start_time
    logger.info(f"Processed by model: {prediction} | Processing time: {response_time:.3f} seconds")

    return {"prediction": prediction, "response_time": f"{response_time:.3f} seconds"}
