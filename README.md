# 🏛️ Court-Data Fetcher & Mini Dashboard

A Python Flask web app that allows users to search Indian court case metadata and view/download the latest judgment.

---

## 📌 Objective

Built as part of the **Think Act Rise Foundation Internship - Task 1**.

This tool helps fetch court case details using case type, number, and filing year, and displays the metadata and latest order/judgment (PDF download enabled).

---

## 🏛️ Target Court

For demo purposes, this project uses **mock data** simulating scraping from the **Delhi High Court** portal:  
🔗 [https://delhihighcourt.nic.in/](https://delhihighcourt.nic.in/)

> (CAPTCHA bypass or real scraping can be added later.)

---

## 🔧 Tech Stack

- Python 3
- Flask
- SQLite
- Jinja2 (HTML templating)

---

## ⚙️ Features

- Simple search form (case type, number, filing year)
- Backend logic using simulated `scraper.py`
- Stores each search in local SQLite DB
- Mini dashboard to view all past queries
- PDF judgment download from `judgments/` folder
- Error handling for invalid inputs

---

## 🚀 Setup Instructions

1. Clone this repository
🔗 git clone  " https://github.com/greeshavaishnavi09/Court-Data-Fetcher-Mini-Dashboard.git "

2. Create virtual environment  
```bash
python -m venv venv  
.\venv\Scripts\activate # On Windows


3. Install requirements  
```bash
pip install -r requirements.txt


4. Run the app  
```bashven
python app.py



5. Open in browser
🔗 Visit http://127.0.0.1:5000
🔗 Visit http://127.0.0.1:5000/dashboard


---

## 🛠️ CAPTCHA Strategy (Mock)

This app does not support real-time scraping or CAPTCHA solving.
Since real court sites have CAPTCHA and state management, this project currently uses mock data for testing. Future upgrades may include:

Remote CAPTCHA solving (2Captcha, Anti-Captcha)

Manual CAPTCHA token input

Headless browsers (Playwright/Selenium)

---

## 💾 Database

All searches are logged in case_searches.db
Dashboard available at: /dashboard 

---

## 📥 PDF Handling

Place sample judgment file in:
court_dashboard/judgments/sample_judgment.pdf

---


## 🖼️ Sample Output

![Dashboard Screenshot](screenshots/dashboard_sample.png)

---

## 📽️ Demo Video

Watch a complete walk-through of the project here:  
🔗 [Loom Demo – Court Data Fetcher & Mini Dashboard](https://www.loom.com/share/b96b071055924070b0c87ff03c936ff6)

Built for Think Act Rise Foundation Internship – Task 1.

---


##  📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.

---

## ✅ Unit Testing

This project includes a basic unit test to verify the response of the homepage (`/`) route using Flask’s test client.

### 🔍 Test File:
- `test_app.py`

### ⚙️ How to Run the Test

Make sure you have `pytest` installed (already covered if you installed `requirements.txt`). Then run:

```bash
pytest test_app.py

