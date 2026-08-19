# 🥗 NutriScan

> **Smart Nutrition Intelligence at Your Fingertips**  
> Transform the way you track your diet with AI-powered food recognition, real-time macro analysis, and intelligent calorie management.

---

## 🎯 Overview

**NutriScan** is a cutting-edge full-stack application that revolutionizes dietary tracking through artificial intelligence. Simply point your camera at any food item—whether it's a slice of pizza, a juicy burger, or packaged snacks—and instantly receive:

- ✅ **Precise nutritional data** (calories, protein, carbs, fats)
- ✅ **Exercise burn calculations** (how much running to burn those calories)
- ✅ **Smart calorie alerts** (notifications when you exceed daily goals)
- ✅ **Real-time macro tracking** (comprehensive dietary insights)

Perfect for fitness enthusiasts, nutritionists, dieters, and anyone serious about their health.

---

## ✨ Key Features

### 🍔 **Smart Food Recognition**
Identify any food instantly with our advanced AI model:
- 📸 **Live Camera Scanning** – Point and identify food in real-time
- 🖼️ **Image Upload** – Drag-and-drop photos from your device
- 🔍 **Barcode Scanner** – Scan product barcodes for instant packaged food details
- 🤖 **AI-Powered Accuracy** – Powered by HuggingFace's state-of-the-art `nateraw/food` model

### 📊 **Comprehensive Nutrition Analysis**
Get detailed insights about every meal:
- 🔢 **Complete Macros** – Calories, Protein, Carbohydrates, and Fats at a glance
- 📈 **Daily Tracking** – Monitor cumulative intake throughout the day
- ⚡ **Instant Updates** – Real-time nutrition information displayed dynamically
- 💾 **Meal History** – Keep track of what you've scanned

### 🏃 **Calorie Burn Calculator**
Understand the effort needed to offset your meals:
- 💪 **Exercise Estimates** – Calculate running distance/time needed to burn calories
- 🎯 **Personalized Goals** – Set your fitness and dietary targets
- 📱 **Quick Reference** – See burn requirements instantly for any food

### ⚠️ **Intelligent Calorie Alerts**
Stay accountable with smart notifications:
- 🎯 **Daily Limits** – Set personalized calorie goals
- 🔔 **Real-time Alerts** – Get notified when approaching or exceeding limits
- 📊 **Progress Tracking** – Visual indicators of daily consumption vs. goals
- 💡 **Smart Recommendations** – Insights to help you stay on track

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React 18 + Vite + Tailwind CSS |
| **Backend** | Python FastAPI + Uvicorn |
| **AI/ML** | PyTorch + HuggingFace Transformers |
| **Model** | `nateraw/food` (Food Classification) |
| **Camera/Scanner** | WebRTC + Barcode Detection |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (Backend)
- Node.js 14+ (Frontend)
- Git

### 1️⃣ Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload
```

> 💡 **First Run Note**: On initial startup, the AI model will download from HuggingFace (~500MB). This is a one-time process and may take a few minutes.

### 2️⃣ Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Start Vite development server
npm run dev
```

**Access the application**: Open your browser and navigate to `http://localhost:5173`

---

## 📖 How It Works

```
1. 📸 Capture/Upload
   └─> Take a photo or upload food image

2. 🤖 AI Analysis
   └─> Model identifies food and retrieves nutrition data

3. 📊 View Results
   └─> See detailed calories and macros instantly

4. 📈 Track Progress
   └─> Monitor daily intake vs. your goals

5. 🔔 Get Alerts
   └─> Notifications if you exceed daily limits

6. 🏃 Burn Calculator
   └─> Find out exercise needed to burn calories
```

---

## 📱 Usage Examples

**Example 1: Quick Lunch Check**
- Scan a pizza slice → Get 285 calories, 12g protein, 36g carbs, 11g fat
- Calculator shows: ~28 minutes of running to burn it off
- Daily tracker updates automatically

**Example 2: Grocery Shopping**
- Scan product barcode → Get complete nutrition label data
- Compare options side-by-side
- Make informed purchasing decisions

**Example 3: Daily Tracking**
- Set daily goal: 2000 calories
- Scan breakfast, lunch, dinner
- Get alert when approaching limit
- Review daily summary

---

## 🎨 Screenshots & Features

| Feature | Description |
|---------|-------------|
| 🎯 **Intuitive UI** | Clean, modern interface designed for quick scanning |
| ⚡ **Fast Processing** | Get results in under 1 second |
| 📊 **Visual Analytics** | Easy-to-read charts and progress indicators |
| 🔒 **Privacy Focused** | Local processing, no unnecessary data collection |

---

## 🛣️ Roadmap

- [ ] Mobile app (iOS/Android)
- [ ] User accounts & cloud sync
- [ ] Dietary preferences & restrictions
- [ ] Meal planning features
- [ ] Restaurant database integration
- [ ] Export nutrition reports
- [ ] Social sharing features

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 (Python) and ESLint (JavaScript) standards
- Write clear commit messages
- Include relevant issue references
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Feedback

- 🐛 Found a bug? [Open an issue](https://github.com/yashmishra123455/Nutriscan/issues)
- 💡 Have a feature idea? [Start a discussion](https://github.com/yashmishra123455/Nutriscan/discussions)
- 📧 Questions? Reach out via email or create an issue

---

## 🙏 Acknowledgments

- **HuggingFace** for the amazing `nateraw/food` model
- **React & Vite** communities for excellent tools
- **FastAPI** for the high-performance backend framework
- **Contributors** who help make NutriScan better

---

<div align="center">

**Made with ❤️ to help you live a healthier life**

[⭐ Give us a star if you find this helpful!](https://github.com/yashmishra123455/Nutriscan)

</div>
