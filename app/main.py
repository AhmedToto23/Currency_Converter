from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException

from app.models import ConvertRequest, ConvertResponse
from app.services import convert_currency, get_exchange_rates

app = FastAPI(title="Currency Converter API")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/currencies")
def list_currencies():
    try:
        rates = get_exchange_rates()
        return sorted(rates.keys())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/convert", response_model=ConvertResponse)
def convert(data: ConvertRequest):
    try:
        result = convert_currency(
            data.amount,
            data.from_currency.upper(),
            data.to_currency.upper()
        )
        return {
            "amount": data.amount,
            "from_currency": data.from_currency,
            "to_currency": data.to_currency,
            "converted_amount": round(result, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico")
