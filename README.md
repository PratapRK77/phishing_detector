# 🛡️ PhishEye — Website Phishing Detection

PhishEye is a lightweight Flask-based web app that detects phishing websites using machine learning and URL feature analysis. Paste a URL, and the app predicts whether it’s **legitimate** or **phishing** based on 30+ features.

## 🚀 Live Demo

Coming soon via [Render](https://render.com/).

---

## 📦 Features

- ✅ Machine Learning–based URL classifier (XGBoost, Logistic)
- 🔎 Extracts 30+ heuristic-based features from URLs
- 🌐 Simple web interface built with Flask
- 💡 Detailed feature analysis of input URL
- 🧩 Extension-ready and deployable

---

## 🧰 Tech Stack

- Python 3.x
- Flask
- NumPy
- scikit-learn / XGBoost
- WHOIS / URL parsing
- HTML/CSS (Poppins, ScrollReveal.js)

---

## 🧪 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/phish-eye.git
cd phish-eye
```

### 2. Install dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add your trained model

Place your pre-trained `model.pkl` file in the root of the project.

The file should contain:
```python
{
    "model": <trained_model_object>,
    "features": <feature_names>
}
```

---

### 4. Run locally

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Deployment (Render)

1. Push this repo to GitHub.
2. Go to [https://render.com](https://render.com)
3. Click **New Web Service** → **Connect repo**
4. Fill in:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add `model.pkl` via **Render Dashboard > Shell** or push it to the repo (if allowed).

---

## 📁 Folder Structure

```
phish-eye/
├── app.py
├── feature_extraction.py
├── model.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── shield.svg
```

---

## 📌 To Do

- [ ] Add browser extension
- [ ] Integrate confidence scores
- [ ] Add page scraping for advanced features

---

## 📜 License

MIT License © 2025 [Pratap Kharabe]
