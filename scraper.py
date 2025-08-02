def fetch_case_details(case_type, case_number, filing_year):
    if case_type.lower() == 'w.p.(c)' and case_number == '16854':
        return {
            'case_type': case_type,
            'case_number': case_number,
            'filing_year': filing_year,
            'petitioner': 'Union of India',
            'respondent': 'Arava Gopi Krishna',
            'filing_date': '17-Jul-2025',
            'next_hearing': '01-Aug-2025',
            'judgment_link': 'sample_judgment.pdf'
        }
    else:
        return None
