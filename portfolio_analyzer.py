import json

def get_portfolio_summary(account_id: int):
    """Returns a basic summary of the user's portfolio."""
    return json.dumps({
        "account_id": account_id,
        "balance": 15000,
        "status": "healthy"
    })