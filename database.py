
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

product1 = ('blackout curtains', 9600, 11000)
product2 = ('drawstring curtains', 6400, 9500)
product3 = ('lace curtains', 1500, 5000)
product4 = ('kid curtains', 9600, 11000)

# call the function Loreen,quite an important part of this!!
insert_products(product1)
insert_products(product2)
insert_products(product3)
insert_products(product4)

print("Products inserted")


def insert_sales(sales_details):
    conn = get_connection()  
    cur = conn.cursor()     
    cur.execute(
        "INSERT INTO sales (pid, quantity) VALUES (%s, %s)", sales_details
    )
    conn.commit()
    conn.close()


sale1 = (1, 24)
sale2 = (2, 68)
sale3 = (3, 5)
sale4 = (4, 6)

insert_sales(sale1)
insert_sales(sale2)
insert_sales(sale3)
insert_sales(sale4)

print("sales inserted")


def insert_stock(stock_details):
    conn = get_connection()     
    cur = conn.cursor() 
    cur.execute(
        "INSERT INTO stock (pid, stock_quantity) VALUES (%s, %s)", stock_details
    )
    conn.commit()
    conn.close()

stock1 = (1, 50)
stock2 = (2, 30)
stock3 = (3, 20)
stock4 = (4, 10)

    
insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)
insert_stock(stock4)


print("stock inserted")

# insert users to myduka

# write a query to fetch sales per product:


def sales_per_product():
    conn = get_connection()     
    cur = conn.cursor()
    cur.execute(
        "SELECT p.name,sum(sales.quantity) as total_sales FROM sales JOIN products as p ON sales.pid=p.id GROUP BY p.name ORDER BY total_sales"
    )
    sales = cur.fetchall()

    for row in sales:
        print(f"Product: {row[0]}, total_sales: {row[1]}")
       


sales_per_product()

# write a query to fetch sales per day:


def sales_per_day():
    conn = get_connection()     
    cur = conn.cursor()
    cur.execute(
        "SELECT sales.created_at,sum(sales.quantity) as total_sales FROM sales JOIN products as p ON sales.pid=p.id GROUP BY created_at ORDER BY total_sales"
    )
    sales = cur.fetchall()
    for row in sales:
        print(f"Product: {row[0]},  total_sales: {row[1]}")


sales_per_product()

# write a query to fetch profit per product:
# profit=selling price - buying price
def profit_per_product():
    conn = get_connection()     
    cur = conn.cursor()
    cur.execute("SELECT p.name,SUM((p.selling_price - p.buying_price) * sales.quantity)  AS profit  FROM products as p  JOIN sales ON sales.pid = p.id  GROUP BY p.name  ORDER BY profit ")
    products= cur.fetchall()
    print("profit per product:")
    for row in products:
        print(f"Product: {row[0]}, Profit: {row[1]}")



profit_per_product()

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