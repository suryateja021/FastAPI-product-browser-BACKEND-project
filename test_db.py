import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

try:
    conn = psycopg2.connect("postgresql://neondb_owner:npg_4FMEBlZTV1Pq@ep-curly-darkness-aig82w45.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require")
    cur = conn.cursor()

    cur.execute("SELECT version();")
    version = cur.fetchone()

    print("Connected successfully!")
    print(version)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)