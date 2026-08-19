# NutriScan

NutriScan is a full-stack application that leverages artificial intelligence to help you make informed dietary choices. Scan food items (like pizza, burgers, snacks) using your camera or upload photos, and instantly get detailed nutritional information including calories and macronutrients. NutriScan goes beyond basic nutrition data—it calculates how much exercise you need to burn those calories and alerts you if you've exceeded your daily calorie goals.

## Key Features

### 🍔 Smart Food Recognition
- **Scan Products**: Point your camera at any food item (pizza, burger, packaged snacks, etc.) to instantly identify it
- **Upload Images**: Drag or select food imagery from your filesystem for analysis
- **Barcode Scanner**: Scan product barcodes to retrieve packaged food details instantly
- **AI-Powered**: Uses advanced machine learning (HuggingFace `nateraw/food` model) for accurate food identification

### 📊 Comprehensive Nutrition Data
- **Detailed Macros**: Get instant access to Calories, Protein, Carbohydrates, and Fats
- **Macro Display**: Dynamically updated UI shows all nutritional information at a glance
- **Accurate Tracking**: Real-time updates of your daily nutritional intake

### 🏃 Calorie Burn Calculation
- **Exercise Calculator**: Automatically calculates how much running (or other exercises) you need to do to burn the calories from scanned food items
- **Personalized Insights**: Shows the effort required to offset each meal

### ⚠️ Smart Calorie Alerts
- **Daily Limits**: Set your personal daily calorie goals
- **Real-time Alerts**: Get notified when you've eaten beyond your calorie tracker limit
- **Overage Warnings**: Helps you stay accountable and maintain your dietary goals

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

## How It Works

1. **Scan or Upload**: Take a photo of your food using the webcam or upload an image from your device
2. **AI Analysis**: NutriScan's AI model identifies the food and retrieves nutritional data
3. **View Nutrition**: See detailed calorie and macro information instantly
4. **Track Progress**: Monitor your daily intake against your calorie goals
5. **Get Alerts**: Receive notifications if you exceed your daily calorie limit
6. **Burn Calculator**: Find out how much exercise is needed to burn off those calories

## Tech Stack
- **Frontend Framework**: React with Vite for fast development
- **Styling**: Tailwind CSS for responsive design
- **Backend Framework**: Python FastAPI for high-performance APIs
- **AI/ML**: PyTorch with HuggingFace Transformers (`nateraw/food` model)
- **Image Processing**: Real-time camera feed and barcode scanning capabilities

## Contributing
Contributions are welcome! Feel free to submit issues and enhancement requests.

## License
This project is open source and available under the MIT License.
