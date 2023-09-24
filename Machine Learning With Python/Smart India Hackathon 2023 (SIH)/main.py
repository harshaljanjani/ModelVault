# fmt: off
# Model Deployment: KYC Aadhar Documentation Check Model (SIH)

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import joblib
import numpy as np
from PIL import Image
from io import BytesIO

main = FastAPI()

# Load the saved model
model = joblib.load("Python/SIH/model.sav")

# Define a route for making predictions
@main.post("/predict/")
async def predict(file: UploadFile):
    try:
        # Read the image file and preprocess it
        image_data = await file.read()
        image = Image.open(BytesIO(image_data))
        image = image.resize((64, 64))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        # Make a prediction using the loaded model
        prediction = model.predict(image)

        # Determine the class based on the prediction
        if prediction[0] == 1:
            class_label = "Valid Aadhar"
        else:
            class_label = "Not a Valid Aadhar"

        return JSONResponse(content={"prediction": class_label}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
