from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from datetime import datetime
import threading, time

from . import models, database, schemas, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, url.original_url)

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    if db_url.expiry_date and datetime.utcnow() > db_url.expiry_date:
        raise HTTPException(status_code=410, detail="Link expired")
    db_url.clicks += 1
    db.commit()
    return RedirectResponse(db_url.original_url)

@app.get("/admin")
def admin_page():
    return FileResponse("static/admin.html")

@app.get("/admin/urls", response_model=list[schemas.URLAdmin])
def get_all_urls(db: Session = Depends(get_db)):
    return db.query(models.URL).all()

def delete_expired_links():
    while True:
        db = database.SessionLocal()
        db.query(models.URL).filter(models.URL.expiry_date < datetime.utcnow()).delete()
        db.commit()
        db.close()
        time.sleep(600)

@app.on_event("startup")
def start_cleanup_thread():
    threading.Thread(target=delete_expired_links, daemon=True).start()
