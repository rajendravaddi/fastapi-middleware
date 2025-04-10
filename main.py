from fastapi import FastAPI, UploadFile, File
import requests
from fastapi.responses import JSONResponse

app = FastAPI()

COLAB_URL = "https://be53-34-44-215-91.ngrok-free.app/model-predict"  # Replace with actual ngrok URL


@app.post("/predict")
async def forward_to_colab(file: UploadFile = File(...)):
    files = {'file': (file.filename, await file.read(), file.content_type)}
    response = requests.post(COLAB_URL, files=files)
    return JSONResponse(content=response.json())
