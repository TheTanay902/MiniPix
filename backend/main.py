from fastapi import FastAPI, Path, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import cv2
import numpy as np
from sklearn.decomposition import PCA
from io import BytesIO
import base64
from script import compress

app = FastAPI()

output_dir = "processed_images"
Path(output_dir).mkdir(parents=True, exist_ok=True)

@app.get("/")
async def root():
    return {"message" : "Hello World"}


@app.post("/compress")
async def compress_uploaded_image(image: UploadFile = File(...)):
    image_data = await image.read()
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    compressed_img = compress(img)

    _, compressed_image_data = cv2.imencode('.jpg', compressed_img)
    # compressed_base64 = base64.b64encode(compressed_image_data).decode('utf-8')
    # return JSONResponse(content={"compressed_image": compressed_base64})
    
    # Generate a unique filename for the processed image
    processed_filename = f"{image.filename.split('.')[0]}_compressed.jpg"
    processed_filepath = f"{output_dir}/{processed_filename}"

    # Save the processed image to the temporary directory
    with open(processed_filepath, "wb") as f:
        f.write(compressed_image_data.tobytes())

    return JSONResponse(content={"message": "Image compressed successfully"})

@app.get("/processed_images/{filename}")
async def get_processed_image(filename: str):
    # Construct the path to the processed image
    processed_filepath = f"{output_dir}/{filename}"

    # Check if the file exists
    if not Path(processed_filepath).is_file():
        return JSONResponse(content={"error": "Image not found"}, status_code=404)

    # Return the processed image as a FileResponse
    return FileResponse(processed_filepath, media_type="image/jpeg")
