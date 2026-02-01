# 🔗 URL Shortener Web Application

A full-stack **URL Shortening Web App** built using FastAPI, MySQL, and SQLAlchemy ORM, with an interactive user interface and admin dashboard.

This application converts long URLs into short links, tracks usage analytics, and automatically manages link expiry.

---

## 🚀 Features

- Convert long URLs into short links  
- Automatic redirection to original URL  
- Click tracking for each link  
- Link expiry system  
- Background task to auto-delete expired links  
- Admin dashboard with:
  - ID  
  - Original URL  
  - Short URL  
  - Click count  
  - Created date  
  - Expiry date  
- Responsive user interface  
- API documentation via Swagger UI

---

## 🏗 Tech Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, JavaScript |
| API Testing | Swagger (FastAPI Docs) |

---

## 🧠 How It Works

1. User submits a long URL  
2. System generates a unique short code  
3. URL mapping stored in MySQL  
4. Visiting the short link redirects to the original URL  
5. Each visit increases click count  
6. Links expire after a set time  
7. Background process removes expired records

---

## 📁 Project Structure

```
url_shortner/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│
├── static/
│   ├── index.html
│   └── admin.html
│
└── requirements.txt
```

---

## ▶ How to Run Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start MySQL Server  
Make sure a database named `url_db` exists.

### 3. Run Application

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Access the App

| Page | URL |
|------|-----|
| Main UI | http://127.0.0.1:8000 |
| Admin Dashboard | http://127.0.0.1:8000/admin |
| API Docs | http://127.0.0.1:8000/docs |

---

## 🎯 Learning Outcomes

This project demonstrates:

- REST API development  
- Database schema design  
- ORM integration  
- Background task handling  
- Full-stack web integration  
- Admin dashboard analytics

---

## 🔮 Future Enhancements

- User authentication  
- Custom short codes  
- Analytics charts  
- Caching for performance  
- Cloud deployment

---

**Author:** JAYSINH THAKOR  
Backend & Web Development Project
