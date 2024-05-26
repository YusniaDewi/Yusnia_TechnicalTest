import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="customers_order"
)

cursor = conn.cursor()

query = """
    SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
           COUNT(o.order_id) AS total_orders,
           SUM(o.amount) AS total_amount_orders
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
    HAVING total_amount_orders >= 500;
"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()