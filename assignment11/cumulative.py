# Task 2
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
# Connect to database
with sqlite3.connect("../db/lesson.db") as conn:
    query = """
    SELECT 
    orders.order_id,
    SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
    ORDER BY orders.order_id;
    """
    df = pd.read_sql(query, conn)

# Create cumulative revenue column
df["cumulative"] = df["total_price"].cumsum()

df.plot(x="order_id", y="cumulative", kind="line", color="green")
plt.title("Cumulative Revenue Over Time")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.show()