import sqlite3

def init_db():
    conn = sqlite3.connect('case_searches.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_search(case_type, case_number, filing_year):
    conn = sqlite3.connect('case_searches.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO searches (case_type, case_number, filing_year)
        VALUES (?, ?, ?)
    ''', (case_type, case_number, filing_year))
    conn.commit()
    conn.close()


