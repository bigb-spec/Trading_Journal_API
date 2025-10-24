<h1 align="center">📊 Trading Journal API</h1>
<p align="center">
  <strong>By BigB Capital</strong> 
</p>
<p align="center">
  <em>A RESTful backend for recording, tracking, and analyzing trading performance.</em>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Desktop-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Backend-API-blue?style=for-the-badge"/>
</p>

---

# 🧾 Trading Journal API

A **Django REST Framework**–powered backend for logging, tracking, and analyzing forex trades.  
It supports **JWT authentication**, **trade management**, and **analytics tracking** — all containerized with **Docker** for seamless deployment.

---

## 🌍 Live Demo

👉 **[bigb.pythonanywhere.com](https://bigb.pythonanywhere.com)**

---

## 🚀 Features
✅ JWT Authentication (Register, Login, Logout)  
✅ CRUD Operations for Trades  
✅ Auto-association of Trades with Logged-in Users  
✅ Session Categorization (Asian, London, New York)  
✅ RESTful JSON Endpoints for Frontend or Postman Testing  
✅ Swagger & Redoc API Docs  
🐳 Dockerized Setup for Easy Deployment  
📊 Analytics Module

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/trading-journal-api.git
cd trading-journal-api
```

---

## 🐳 Docker Setup

### Option A — Run Entire App with Docker
```bash
docker-compose up --build
```
This will:
- Build your image  
- Run database migrations automatically  
- Expose the API on `http://localhost:8000`

### 2️⃣ Run migrations and create superuser

```bash
docker exec -it trading_django python manage.py makemigrations
docker exec -it trading_django python manage.py migrate
docker exec -it trading_django python manage.py createsuperuser

```

To stop:
```bash
docker-compose down
```

### Option B — Manual Container Commands
```bash
docker build -t trading_journal_api .
docker run -p 8000:8000 trading_journal_api
```

---

## 🧩 Environment Variables

Create a `.env` file in the root directory:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 🧠 Manual Setup (Without Docker)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

App runs at:
```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Endpoints

### Register
```
POST /api/accounts/register/
```
**Body:**
```json
{
  "username": "brandon",
  "email": "brandon@example.com",
  "password": "StrongPass123",
  "password2": "StrongPass123"
}
```

### Login
```
POST /api/accounts/login/
```
**Body:**
```json
{
  "username": "brandon",
  "password": "StrongPass123"
  "password2": "StrongPass123"
}
```

**Response:**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```

Use in headers:
```
Authorization: Bearer <your-token>
```

---

## 💹 Trade Management Endpoints

### List Trades
```
GET /api/trades/trades/
```

### Create Trade
```
POST /api/trades/trades/
```
**Body:**
```json
{
  "symbol": "GBPUSD",
  "direction": "SELL",
  "session": "NEW YORK",
  "entry_price": 1.27,
  "exit_price": 1.27,
  "result": "WIN",
  "notes": "Short after liquidity grab",
  "date": "2025-10-18T14:30:00Z"
}
```

---

## 📊 Analytics (Coming Soon)
Endpoints will support:
- Win rate tracking by session  
- RR performance analysis  
- Trade statistics aggregation

---

## 🔍 Testing with Postman

### Step 1 — Login
Retrieve your JWT token.

### Step 2 — Add Header
```
Authorization: Bearer <your-token>
```

### Step 3 — Test Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/accounts/register/` | Register new user |
| POST | `/api/accounts/login/` | Login and get token |
| GET | `/api/trades/trades/` | List trades |
| POST | `/api/trades/trades/` | Create new trade |
| GET | `/api/analytics/summary/` | Analytics |

📸 **Adding Screenshots in Postman Tests:**
- Run the request in Postman  
- Click **“Save Response → Save to File”** or take a **screenshot**  
- Save images in a `/screenshots` directory  
- Link in README using markdown:
```markdown
![Postman Screenshot](screenshots/test_register.png)
```

---

## 📘 API Documentation

| Tool | URL |
|------|-----|
| Swagger | `http://127.0.0.1:8000/swagger/` |
| Redoc | `http://127.0.0.1:8000/redoc/` |

---

## 🧰 Tech Stack
- Python 3.12+
- Django 5.x
- Django REST Framework
- SimpleJWT
- MYSQL
- Docker + Docker Compose

---

## 🧱 Project Structure
```
Trading_Journal_API/
│
├── accounts/          # Authentication app
├── trades/            # Trade logic
├── analytics/         # Stats logic (coming soon)
├── trading_journal/   # Settings
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```


## 👤 Author
**Brandon Kiprotich**  
Architect | Backend Developer | Forex Trader  
🔗 [LinkedIn](https://www.linkedin.com/in/brandonkiprotich)  
🌐 [Portfolio](https://sites.google.com/view/brandonkiprotich/home)
