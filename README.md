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

Trading Journal API - Documentation

# 🧾 Trading Journal API

A Django REST Framework–based backend for managing and tracking forex trades — allowing users to register, log trades, upload screenshots, and analyze performance metrics.

---

## 🚀 Features
- User authentication (JWT-based)
- Record trades (pair, session, direction, etc.)
- Upload and view screenshots of trades
- API documentation via Swagger and ReDoc
- Dockerized environment for easy setup

---

## 🧰 Installation

### 1. Clone the Repository
```
git clone https://github.com/yourusername/Trading_Journal_API.git
cd Trading_Journal_API
```

### 2. Create and Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # on Windows
# OR
source venv/bin/activate   # on Mac/Linux
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (optional)
```
python manage.py createsuperuser
```

### 6. Run Server
```
python manage.py runserver
```

---

## 🐳 Using Docker

### Build and Run
```
docker-compose up --build
```
Your API will be available at:  
👉 **http://localhost:8000**

---

## 📚 API Documentation

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
- **ReDoc UI:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 🧪 Testing with Postman

You can test all API endpoints using **Postman**.

### 1. Register a User
**POST** `http://localhost:8000/api/accounts/register/`
```json
{
  "username": "trader1",
  "email": "trader1@example.com",
  "password": "strongpassword123"
}
```

### 2. Login
**POST** `http://localhost:8000/api/accounts/login/`
```json
{
  "username": "trader1",
  "password": "strongpassword123"
}
```
Copy the returned token and use it as a **Bearer Token** in all authorized requests.

### 3. Create a Trade
**POST** `http://localhost:8000/api/trades/trades/`
Use **form-data** body:

| Key | Value | Type |
|------|--------|------|
| pair | EURUSD | Text |
| direction | BUY | Text |
| session | New York | Text |
| entry_price | 1.0734 | Text |
| exit_price | 1.0760 | Text |
| profit_loss | 26 | Text |
| screenshot | (select file) | File |

🖼 **Adding a Screenshot in Postman:**
1. In request body, select **form-data**.  
2. Add `screenshot` key.  
3. Change type to **File**.  
4. Click **Select Files** → choose your image.  
5. Click **Send** → you’ll get a `201 Created` response.

### 4. List All Trades
**GET** `http://localhost:8000/api/trades/trades/`

### 5. Retrieve a Single Trade
**GET** `http://localhost:8000/api/trades/trades/<trade_id>/`

### 6. Update or Delete a Trade
**PATCH / DELETE** `http://localhost:8000/api/trades/trades/<trade_id>/`

---

## 💡 Lessons & Challenges
- Structured Django REST APIs with JWT authentication.
- Implemented Docker for easy deployment.
- Integrated Swagger and ReDoc documentation.
- Improved secret handling and Git best practices.
- Learned media upload configuration and debugging.

