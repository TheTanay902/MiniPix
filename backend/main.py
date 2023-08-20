from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from sklearn.decomposition import PCA
from io import BytesIO
import base64
from script import compress

app = FastAPI()


@app.post("/compress")
async def compress_uploaded_image(image: UploadFile = File(...)):
    image_data = await image.read()
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    compressed_img = compress(img)

    _, compressed_image_data = cv2.imencode('.jpg', compressed_img)
    compressed_base64 = base64.b64encode(compressed_image_data).decode('utf-8')

    return JSONResponse(content={"compressed_image": compressed_base64})