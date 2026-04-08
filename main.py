from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()

def calculate_lcm(x, y):
    if x == 0 or y == 0:
        return 0
    # Formula: |a*b| / gcd(a,b)
    return abs(x * y) // math.gcd(x, y)

@app.get("/ysalohiddin02_gmail_com", response_class=PlainTextResponse)
async def get_lcm(x: str = None, y: str = None):
    # Check if parameters are missing or contain non-digit characters (handles negatives/decimals)
    if x is None or y is None or not (x.isdigit() and y.isdigit()):
        return "NaN"
    
    try:
        val_x = int(x)
        val_y = int(y)
        
        result = calculate_lcm(val_x, val_y)
        return str(result)
    except Exception:
        return "NaN"