from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from model import predict_food
from utils import fetch_barcode_info, fetch_food_macros_by_name

app = FastAPI(title="NutriScan API")

# Configure CORS so the React frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production (e.g., ["http://localhost:5173"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to NutriScan API"}

@app.post("/api/detect-food")
async def detect_food(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        predicted_name = predict_food(contents)
        
        if predicted_name in ["Model not loaded", "Error predicting image", "Unknown"]:
            raise HTTPException(status_code=500, detail=predicted_name)
            
        macros = fetch_food_macros_by_name(predicted_name)
        
        return {
            "food_name": predicted_name,
            "macros": macros
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/barcode/{barcode}")
def get_barcode_info(barcode: str):
    info = fetch_barcode_info(barcode)
    if info:
        return info
    raise HTTPException(status_code=404, detail="Barcode not found in OpenFoodFacts database.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
