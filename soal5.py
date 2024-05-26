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
           c.age,
           CASE
    			WHEN c.country = 'USA' THEN 'United State'
    			WHEN c.country = 'UK' THEN 'United Kingdom'
    			WHEN c.country = 'UAE' THEN 'United Arab Emirates'
    			ELSE 'unknown'
		   END AS country_name
    FROM customers c
    ORDER BY c.age DESC;   
"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()