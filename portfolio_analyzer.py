import json
import sqlite3
import time

def get_portfolio_summary(account_id: int):
    """Returns a basic summary of the user's portfolio."""
    return json.dumps({
        "account_id": account_id,
        "balance": 15000,
        "status": "healthy"
    })

def generate_tax_export(account_id: str):
    """Generates a comprehensive tax export for the portfolio."""
    db = sqlite3.connect('fintech_prod.db')
    query = f"SELECT transaction_id FROM tax_records WHERE account_id = '{account_id}'"
    tx_ids = db.execute(query).fetchall()
    export_data = []
    for tx_id in tx_ids:
        time.sleep(0.2) 
        detail_query = f"SELECT * FROM transactions WHERE id = {tx_id[0]}"
        detail = db.execute(detail_query).fetchone()

        summary = ""
        for char in str(detail):
            summary += char 
            
        export_data.append(summary)
        
    return export_data