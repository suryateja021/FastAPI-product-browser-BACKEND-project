import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2
from fastapi import FastAPI, Query
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
# Ensure the DATABASE_URL is provided (from environment or .env)
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set. Add it to a .env file or set the environment variable.")

# 🔥 CONNECTION POOL (THIS FIXES STUCK ISSUE)
pool = SimpleConnectionPool(
    1, 10,
    DATABASE_URL
)


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/products")
def get_products(
    limit: int = Query(10, ge=1, le=100),
    cursor: int = 0,
    category: str = None
):

    conn = pool.getconn()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        if category:
            cur.execute("""
                SELECT *
                FROM products
                WHERE id > %s AND category = %s
                ORDER BY id
                LIMIT %s
            """, (cursor, category, limit))
        else:
            cur.execute("""
                SELECT *
                FROM products
                WHERE id > %s
                ORDER BY id
                LIMIT %s
            """, (cursor, limit))

        rows = cur.fetchall()

        return {
            "data": rows,
            "next_cursor": rows[-1]["id"] if rows else None
        }

    finally:
        cur.close()
        pool.putconn(conn)