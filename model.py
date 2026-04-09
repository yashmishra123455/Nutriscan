from transformers import pipeline
from PIL import Image
import io

print("Loading Food Classification Model... (This may take a moment to download weights)")
try:
    classifier = pipeline("image-classification", model="nateraw/food")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
    classifier = None

def predict_food(image_bytes: bytes) -> str:
    if classifier is None:
        return "Model not loaded"
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        results = classifier(image)
        if results and len(results) > 0:
            return results[0]['label']
        return "Unknown"
    except Exception as e:
        print(f"Prediction Error: {e}")
        return "Error predicting image"
