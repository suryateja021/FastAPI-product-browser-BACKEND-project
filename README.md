# 📦 FastAPI Product Browser API

A high-performance backend API built with FastAPI and PostgreSQL (Neon DB) that serves a large dataset of products (200,000+ records) with pagination and filtering.

https://github.com/suryateja021/FastAPI-product-browser-BACKEND-project.git

---

## 🚀 Features

- FastAPI backend
- PostgreSQL (Neon cloud database)
- 200,000+ products dataset
- Cursor-based pagination
- Category filtering (Books, Electronics, Sports, Clothes)
- Bulk data seeder using batch inserts
- Environment variable support (.env)
- Swagger API documentation

---

## 🏗️ Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL (Neon)
- psycopg2
- python-dotenv

---

## 📁 Project Structure


product-browser/
│
├── main.py
├── seed.py
├── test_db.py
├── .env
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/suryateja021/FastAPI-product-browser-BACKEND-project.git
cd FastAPI-product-browser-BACKEND-project
2. Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install fastapi uvicorn psycopg2-binary python-dotenv
4. Create .env file
DATABASE_URL=your_neon_database_url_here
5. Run database seeder (optional)
python seed.py

This will insert 200,000 products.

6. Start server
uvicorn main:app --reload
🌐 API Endpoints
🔹 Health Check
GET /

Response:

{
  "status": "ok"
}
🔹 Get Products (Pagination)
GET /products?limit=10&cursor=0

Response:

{
  "data": [],
  "next_cursor": 10
}
🔹 Filter by Category
GET /products?category=Books&limit=10

📌 Query Parameters
Parameter	Type	Description
limit	int	Number of products (default: 10)
cursor	int	Pagination cursor
category	string	Filter products by category

📖 API Docs
Swagger UI:
http://127.0.0.1:8000/docs

🔐 Environment Variables
Variable	Description
DATABASE_URL	PostgreSQL connection string

🚀 Future Improvements
Add Redis caching
Add authentication (JWT)
Dockerize project
Async FastAPI upgrade
Frontend UI

⭐ If you like this project
Give it a star ⭐ on GitHub!
