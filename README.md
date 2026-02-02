# 🌐 URL Shortener Web Application  
FastAPI + MySQL + Cloud-Scalable AWS Deployment

A full-stack URL Shortening Web App built using FastAPI, MySQL, and SQLAlchemy ORM, enhanced with cloud deployment, load balancing, auto scaling, and serverless automation.

---

## 🚀 Project Overview

This application converts long URLs into short links, tracks usage analytics, and automatically manages link expiry.  
The system is designed as both a **full-stack web project** and a **cloud-native scalable architecture**.

---

## ✨ Core Features

- Convert long URLs into short links  
- Automatic redirection to original URL  
- Click tracking  
- Link expiry system  
- Background task to auto-delete expired links  
- Admin dashboard displaying:
  - ID  
  - Original URL  
  - Short URL  
  - Click count  
  - Created date  
  - Expiry date  
- Responsive UI  
- API documentation via Swagger  

---

## 🧰 Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | FastAPI |
| Database | MySQL (Local) / PostgreSQL (AWS RDS) |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker |
| Hosting | AWS EC2 |
| Load Balancing | Application Load Balancer |
| Auto Scaling | AWS Auto Scaling Group |
| Automation | AWS Lambda |
| Scheduler | Amazon EventBridge |
| Monitoring | Amazon CloudWatch |

---

## 🧠 How It Works

1. User submits long URL  
2. System generates unique short code  
3. URL mapping stored in database  
4. Visiting short link redirects  
5. Click count increases  
6. Links expire after set time  
7. Background system removes expired links  

---

## 📁 Project Structure

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
├── Dockerfile
└── requirements.txt

---

## 🖥️ Run Locally

pip install -r requirements.txt  
uvicorn app.main:app --reload  

| Page | URL |
|------|-----|
| Main UI | http://127.0.0.1:8000 |
| Admin | http://127.0.0.1:8000/admin |
| API Docs | http://127.0.0.1:8000/docs |

---

# ☁️ Cloud Deployment Architecture

User → Application Load Balancer → EC2 (Docker App) → RDS Database  
EventBridge → Lambda → RDS Cleanup

---

## ☁️ Quick Cloud Deployment Reference

1. Dockerize application  
2. Push image to Docker Hub  
3. Launch EC2 instance  
4. Create database in RDS  
5. Run container on EC2  
6. Configure Application Load Balancer  
7. Setup Auto Scaling  
8. Create Lambda cleanup function  
9. Schedule using EventBridge  
10. Monitor via CloudWatch  

---

## 📊 Cloud Features Added

- High availability deployment  
- Horizontal scaling  
- Load balancing  
- Serverless database cleanup  
- Cloud monitoring  

---

## 🧪 Testing

| Feature | How to Test |
|---------|-------------|
| Load Balancer | Refresh `/server` |
| Auto Scaling | Generate heavy load |
| Lambda | Check cleanup logs |

---

## 💰 Cloud Status

Cloud infrastructure may be stopped to avoid charges.  
Deployment instructions remain for re-use.

---

## 🎯 Learning Outcomes

- REST API development  
- Full-stack integration  
- ORM and database design  
- Docker containerization  
- Cloud architecture & scaling  
- Serverless automation  

---

## 🔮 Future Enhancements

- User authentication  
- Custom short codes  
- Analytics dashboards  
- Caching layer  
- Advanced security  

---

## 👨‍💻 Author

**Jaysinh Thakor**  
Backend & Cloud Developer
