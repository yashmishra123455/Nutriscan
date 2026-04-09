# NutriScan

NutriScan is a full-stack application that leverages artificial intelligence to identify food from photos and retrieve accurate macronutrient data. It also features a barcode scanner that extracts nutritional info using the OpenFoodFacts API.

## Architecture
- **Frontend**: React (Vite) + Tailwind CSS
- **Backend**: Python (FastAPI) + PyTorch / Transformers (HuggingFace `nateraw/food` model)

## How to Run

### 1. Backend Setup
1. Open a new terminal and navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. (Optional but recommended) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
*(Note: The first time you start the backend and make a request, the AI model weights will be downloaded from huggingface, which may take a few minutes.)*

### 2. Frontend Setup
1. Open a second terminal and navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
4. Open the displayed local URL (typically `http://localhost:5173`) in your browser to use NutriScan!

## Features
- **Upload Image**: Drag or select food imagery from your filesystem.
- **Webcam Capture**: Live camera feed to take photos directly in the browser.
- **Barcode Scanner**: Present a barcode to the camera to get instant packaged food details.
- **Macros Display**: Dynamically updates UI to show Calories, Protein, Carbs, and Fats.
