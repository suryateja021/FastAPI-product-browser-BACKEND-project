import psycopg2
import random
from datetime import datetime
from psycopg2.extras import execute_values

DATABASE_URL = "postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect("postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require")
cur = conn.cursor()

categories = ["Books", "Electronics", "Sports", "Clothes"]

TOTAL_ROWS = 200000
BATCH_SIZE = 5000

batch = []
now = datetime.now()

print("Starting insert...")

for i in range(1, TOTAL_ROWS + 1):

    batch.append((
        f"Product {i}",
        random.choice(categories),
        random.randint(100, 5000),
        now,
        now
    ))

    if len(batch) == BATCH_SIZE:
        execute_values(
            cur,
            """
            INSERT INTO products (name, category, price, created_at, updated_at)
            VALUES %s
            """,
            batch
        )
        conn.commit()
        batch.clear()

        print(f"Inserted {i} rows")

# final batch
if batch:
    execute_values(
        cur,
        """
        INSERT INTO products (name, category, price, created_at, updated_at)
        VALUES %s
        """,
        batch
    )
    conn.commit()

print("DONE: 200,000 products inserted")

cur.close()
conn.close()