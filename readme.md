# 💱 Currency Converter Web App

A modern **Currency Converter** web application that allows users to convert amounts between different currencies using **real-time exchange rates**, with **country flags displayed inside the currency dropdown lists** for an enhanced user experience.

---

## ✨ Features

- 🌍 Real-time currency conversion
- 🔁 Convert between multiple currencies
- ⚡ Fast and lightweight UI
- 🔌 RESTful API integration
- 📱 Responsive design

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla JS)

### Backend
- Python
- FastAPI
- REST API

### External Resources
- Flag images from **flagcdn.com**
- Exchange rate API (configured in backend)

---

## 📂 Project Structure

currency-converter/
│
├── static/
│ ├── style.css
│ ├── script.js
│
├── templates/
│ └── index.html
│
├── main.py
├── requirements.txt
└── README.md


---

## 🚀 How to Run Locally

1️⃣ Clone the repository

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI server
uvicorn main:app --reload

5️⃣ Open in browser
http://127.0.0.1:8000



📌 Example Currencies Supported

USD – United States 🇺🇸

EUR – Eurozone 🇪🇺

GBP – United Kingdom 🇬🇧

EGP – Egypt 🇪🇬

JPY – Japan 🇯🇵

SAR – Saudi Arabia 🇸🇦


👨‍💻 Author

Ahmed Toto
