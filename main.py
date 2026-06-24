import psycopg2
from fastapi import FastAPI, Query
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

app = FastAPI()

DATABASE_URL = "postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

# 🔥 CONNECTION POOL (THIS FIXES STUCK ISSUE)
pool = SimpleConnectionPool(
    1, 10,
    "postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"
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