from fastapi import FastAPI, File, UploadFile

from ocr_engine import extract_delivery_note_data

app = FastAPI(title="OCR Delivery Note Service")


@app.post("/extract-delivery-note")
async def extract_delivery_note(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return extract_delivery_note_data(image_bytes)
