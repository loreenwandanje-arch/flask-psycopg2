from database import get_products, get_sales, get_stocks, insert_products, insert_user,insert_sales, insert_stock,check_user_exists
import datetime
from flask import Flask, render_template, redirect, request, url_for, flash,session
from flask_bcrypt import Bcrypt
from functools import wraps
# creating a flask instance
app = Flask(__name__)

# bcrypt instance
bcrypt = Bcrypt(app)

app.secret_key = 'myduka2026'

# homepage route
@app.route('/')  # index route,decorater function
def home():  # view function
    return render_template('index.html')

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

# products route
@app.route('/products')
@login_required
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
@login_required
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
       
        check_stock = available_stock(product_id)
        if check_stock < float(quantity):
            flash("Insufficient stock,can't complete sale",'danger')
            return redirect(url_for('sales'))
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))


@app.route('/stocks')
@login_required
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
@login_required
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form ['name']
        email = request.form ['email']
        phone_number = request.form ['phone']
        password = request.form ['password']

        existing_user = check_user_exists(email)
        if not existing_user :
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user =(full_name,email,phone_number,hashed_password)
            insert_user(new_user)
            flash("User Inserted Successfully",'success')
        else:
             flash("User Not Inserted,Try again later",'danger')
    return render_template('register.html')
        
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            flash("User doesn't exist,please register",'danger')
        else:
            if bcrypt.check_password_hash(existing_user[-1],password):
                session['email'] = email
                flash("Login successful",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect",'danger')
    
    return render_template('login.html')


# #List Comprehension
# # TASK 1-Create a list of squares from 1 to 10
squares = [x**2 for x in range(10)]
print(squares)

# TASK 2-words= ["apple","mango","kiwi","egg","cherry","bread","me"]-create a new list of words that have length >=5
words= ["apple","mango","kiwi","egg","cherry","bread","me"]
new_words = [i for i in words if len(i) >=5]
print(new_words)

# # run the program
# app.run(debug=True)
