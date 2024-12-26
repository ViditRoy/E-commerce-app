from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ecommerce",
    user="postgres",
    password="password",
    host="localhost"
)
cursor = conn.cursor()

@app.get("/analytics/revenue")
def get_total_revenue():
    cursor.execute("SELECT SUM(price) FROM transactions")
    total_revenue = cursor.fetchone()[0]
    return {"total_revenue": total_revenue}

@app.get("/analytics/top-products")
def get_top_products():
    cursor.execute("""
        SELECT product_id, COUNT(*) as sales
        FROM transactions
        GROUP BY product_id
        ORDER BY sales DESC
        LIMIT 5
    """)
    top_products = cursor.fetchall()
    return {"top_products": top_products}
