from pydantic import BaseModel
from datetime import datetime

class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_url: str
    model_config = {"from_attributes": True}

class URLAdmin(BaseModel):
    id: int
    original_url: str
    short_code: str
    clicks: int
    created_at: datetime | None = None
    expiry_date: datetime | None = None
    model_config = {"from_attributes": True}
