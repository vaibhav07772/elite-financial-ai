import re

def calculate_ratios(text):
    text = text.lower()
    
    result = {}
    
    if "debt" in text and "equity" in text:
        result["Debt/Equity"] = "High (approx)"
    
    if "liabilities" in text and "assets" in text:
        result["Risk"] = "Moderate"
    
    return result