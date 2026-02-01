import random, string
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import models

BASE_URL = "http://localhost:8000"

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(db: Session, original_url: str):
    code = generate_code()
    db_url = models.URL(
        original_url=original_url,
        short_code=code,
        expiry_date=datetime.utcnow() + timedelta(hours=1)
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return {"short_url": f"{BASE_URL}/{code}"}

def get_url(db: Session, code: str):
    return db.query(models.URL).filter(models.URL.short_code == code).first()
