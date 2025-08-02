from flask import Flask, render_template, request, send_from_directory
from scraper import fetch_case_details
from db import init_db, save_search
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    # ✅ Fetch the result first
    result = fetch_case_details(case_type, case_number, filing_year)

    if result is None:
        # ❌ If not found, show error message in result.html
        return render_template('result.html', error="❌ Case not found or court website is down.")

    # ✅ Save only valid submissions
    save_search(case_type, case_number, filing_year)
    return render_template('result.html', result=result)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(app.root_path, 'judgments'), filename)

@app.route('/dashboard')
def dashboard():
    import sqlite3
    conn = sqlite3.connect('case_searches.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM searches ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', rows=rows)

# ✅ Initialize database before running app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

