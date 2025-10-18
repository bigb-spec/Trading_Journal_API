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

## 🧭 Overview

The **Trading Journal API** provides a structured and secure way for traders to log, review, and analyze their trades.  
Built using **Django Rest Framework**, it offers authentication, data validation, and easy containerization via Docker.  

> _"Precision. Discipline. Execution."_ — **BigB Capital**

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Framework** | Django Rest Framework |
| **Database** | MySQL |
| **Containerization** | Docker & Docker Compose |
| **API Docs** | Swagger UI / Redoc |
| **Authentication** | JWT (JSON Web Token) |
| **Language** | Python 3.11+ |

---

## 🧩 Project Structure

Trading_Journal_API/


├── account/ # User registration, login, authentication logic

├── trades/ # Core app handling trade data

├── trading_journal_api/ # Root configuration & settings

 ├──├── settings.py # Configures environment variables from .env

│

├── Dockerfile

├── docker-compose.yml

├── .env.example

├── requirements.txt

└── README.md

---

## 🐳 Docker Setup

Ensure **Docker Desktop** is running, then build and launch containers:

```bash
docker compose up --build
Services:

Django API: http://localhost:8000

Adminer (DB UI): http://localhost:8080

Credentials (from .env):

Host: db

User: root

Password: yourpassword

🔐 Environment Variables
Create a .env file at the project root:

env
Copy code
SECRET_KEY=your-production-secret
DEBUG=True
ALLOWED_HOSTS=*

MYSQL_DATABASE=trading_journal
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_ROOT_PASSWORD=yourpassword
MYSQL_HOST=db
MYSQL_PORT=3306
✅ Always exclude .env from version control via .gitignore.

📚 API Documentation
Once running:

Swagger UI: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/

🔑 Example Endpoints
Endpoint	Method	Description

/api/register/	POST	Register new user

/api/login/	POST	Obtain JWT tokens

/api/trades/	GET/POST	Retrieve or create trade records

/api/trades/{id}/	PUT/DELETE	Update or delete a trade

🧠 Security & Best Practices
Keep SECRET_KEY and DB credentials outside the repo.

Use .env for sensitive info.

Use HTTPS in production.

Regularly rotate credentials.

🚀 Future Enhancements
Real-time trading analytics (PnL, Win Rate, RR)

Broker API integration (MT5, cTrader)

AI trade insight module

Multi-user portfolio dashboards

🧾 License
This project is owned and maintained by BigB Capital.
All rights reserved © 2025.
