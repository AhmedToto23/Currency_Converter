from pydantic import BaseModel, Field

class ConvertRequest(BaseModel):
    amount: float = Field(gt=0)
    from_currency: str
    to_currency: str

class ConvertResponse(BaseModel):
    amount: float
    from_currency: str
    to_currency: str
    converted_amount: float
