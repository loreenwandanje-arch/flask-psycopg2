import psycopg2

# Establish a database connection.
conn = psycopg2.connect(host='localhost', port='5432',
                        user='postgres', password='076912lor', dbname='myduka')

# object for db operations
cur = conn.cursor()

# insert products to myduka db
# use a parameter(product_details) to make it reusable


def insert_products(product_details):
    # i used on confict do nothing to prevent duplicate data
    cur.execute(
        "INSERT INTO products (name, buying_price, selling_price) VALUES (%s, %s,%s)", product_details)
    conn.commit()


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
    cur.execute(
        "INSERT INTO sales (pid,quantity,created_at) VALUES (%s,%s,%s)", sales_details)
    conn.commit()


sale1 = (1, 24, '10/1/2023')
sale2 = (2, 68, '11/2/2023')
sale3 = (3, 5, '10/1/2023')
sale4 = (4, 6, '06/1/2023')

insert_sales(sale1)
insert_sales(sale2)
insert_sales(sale3)
insert_sales(sale4)

print("sales inserted")


def insert_stock(stock_details):
    cur.execute(
        "INSERT INTO stock (pid,stock_quantity,created_at) VALUES (%s,%s,%s)", stock_details)
    conn.commit()


stock1 = (1, 24, '10/1/2023')
stock2 = (2, 68, '11/2/2023')
stock3 = (3, 5, '10/1/2023')
stock4 = (4, 6, '06/1/2023')

insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)
insert_stock(stock4)

print("stock inserted")

# insert users to myduka


def insert_users(user_details):
    cur.execute(
        "INSERT INTO users (full_name,email,phone_number,password) VALUES (%s,%s,%s,%s) ON CONFLICT (email) DO NOTHING", user_details)
    conn.commit()


user1 = ('Jamie Taka', 'jamietake24@gmail.com', '0712345678', '000Takejam')
user2 = ('Miles Morales', 'spiderweb67@gmail.com', '0769125054', '12345678')
user3 = ('James Hugh', 'hughgrant@gmail.com', '07569087623', 'treats45')
user4 = ('Mary Glaze', 'glazedmaria5@gmail.com', '0774567890', 'mary1mary')

# call the function/very important
insert_users(user1)
insert_users(user2)
insert_users(user3)
insert_users(user4)

print("users inserted!")

# write a query to fetch sales per product:


def sales_per_product():
    cur.execute(
        "SELECT p.name,sum(sales.quantity) as total_sales FROM sales JOIN products as p ON sales.pid=p.id GROUP BY p.name ORDER BY total_sales"
    )
    sales = cur.fetchall()

    for row in sales:
        print(f"Product: {row[0]}, total_sales: {row[1]}")
       


sales_per_product()

# write a query to fetch sales per day:


def sales_per_day():
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
    cur.execute("SELECT p.name,SUM((p.selling_price - p.buying_price) * sales.quantity)  AS profit  FROM products as p  JOIN sales ON sales.pid = p.id  GROUP BY p.name  ORDER BY profit ")
    products= cur.fetchall()
    print("profit per product:")
    for row in products:
        print(f"Product: {row[0]}, Profit: {row[1]}")



profit_per_product()