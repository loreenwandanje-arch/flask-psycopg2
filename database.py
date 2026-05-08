import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='076912lor',
        dbname='myduka'
    )
    return conn

def get_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return data

def get_sales():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    data = cur.fetchall()
    conn.close()
    return data

def get_stocks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock")
    data = cur.fetchall()
    conn.close()
    return data

def insert_products(product_details):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, buying_price, selling_price) VALUES (%s, %s, %s)", product_details)
    conn.commit()
    conn.close()

def insert_sales(sales_details):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO sales (pid, quantity) VALUES (%s, %s)", sales_details)
    conn.commit()
    conn.close()

def insert_stock(stock_details):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO stock (pid, stock_quantity) VALUES (%s, %s)", stock_details)
    conn.commit()
    conn.close()

def insert_user(user_details):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (full_name, email, phone_number, password) VALUES (%s, %s, %s, %s)", user_details)
    conn.commit()
    conn.close()

def check_user_exists(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE users.email = %s", (email,))
    user_data = cur.fetchone()
    conn.close()
    return user_data

def sales_per_product():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.name, SUM(sales.quantity) AS total_sales 
        FROM sales 
        JOIN products AS p ON sales.pid = p.id 
        GROUP BY p.name 
        ORDER BY total_sales
    """)
    sales = cur.fetchall()
    conn.close()
    return sales

def sales_per_day():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT sales.created_at, SUM(sales.quantity) AS total_sales 
        FROM sales 
        JOIN products AS p ON sales.pid = p.id 
        GROUP BY created_at 
        ORDER BY total_sales
    """)
    sales = cur.fetchall()
    conn.close()
    return sales

def profit_per_product():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.name, SUM((p.selling_price - p.buying_price) * sales.quantity) AS profit 
        FROM products AS p 
        JOIN sales ON sales.pid = p.id 
        GROUP BY p.name 
        ORDER BY profit
    """)
    products = cur.fetchall()
    conn.close()
    return products

def profit_per_day():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT sales.created_at, SUM((p.selling_price - p.buying_price) * sales.quantity) AS total_profit 
        FROM sales 
        JOIN products p ON sales.pid = p.id 
        GROUP BY sales.created_at 
        ORDER BY sales.created_at ASC
    """)
    results = cur.fetchall()
    conn.close()
    return results