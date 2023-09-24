# fmt: off
# Model: Product Listing Algorithm (SIH)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import onnxruntime
import numpy as np

onnx_path = "Python\SIH\product_ranking_model.onnx"
session = onnxruntime.InferenceSession(onnx_path)

app = FastAPI()

class InputData(BaseModel):
    data: list
    total_products: int

class PredictionResponse(BaseModel):
    final_predicted_rank: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: InputData):
    try:
        input_data_array = np.array(input_data.data, dtype=np.float32)
        input_data_array = input_data_array.reshape((1, -1))

        input_name = session.get_inputs()[0].name
        input_tensor = {input_name: input_data_array}

        output_name = session.get_outputs()[0].name
        result = session.run([output_name], input_tensor)

        predictions = result[0]

        final_rank = float(predictions[0] * input_data.total_products)

        return {"final_predicted_rank": final_rank}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
