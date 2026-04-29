from database import get_products, get_sales, get_stocks, insert_products, insert_sales, insert_stock,available_stock
import datetime
from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = 'myduka2026'

@app.route('/')  # index route,decorater function
def home():  # view function
    return render_template('index.html')


@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html', products_data=products_data)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name, buying_price, selling_price)
        insert_products(new_product)
        flash("Product added successfully", 'success')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = get_sales()
    products = get_products()
    print("PRODUCTS:", products) 
    return render_template("sales.html",sales_data = sales_data, products_data=products)


@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        print("Sale made successfully",'success')
    return redirect(url_for('sales'))


@app.route('/stocks')
def stocks():
    stock_data = get_stocks()
    product_data = get_products()
    print("PRODUCTS:", products) 
    return render_template('stocks.html', stocks_data=stock_data, product_data=product_data)


@app.route('/add_stocks', methods=['GET', 'POST'])
def add_stocks():
    if request.method == 'POST':
        product_id = request.form['pid']
        stock_quantity = request.form['quantity']
        new_stock = (product_id, stock_quantity)
        insert_stock(new_stock)
        flash("Stock added successfully", 'success')
    return redirect(url_for('stocks'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


# This starts the Flask server so your app is live and listening for visitors.
app.run(debug=True)
