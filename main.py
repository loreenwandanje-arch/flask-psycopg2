import datetime
from flask import Flask,render_template,redirect,request,url_for

app = Flask (__name__)
from database import get_products, get_sales,get_stocks,insert_products,insert_sales,insert_stock

@app.route('/')#index route,decorater function
def home():#view function
    return render_template('index.html')

@app.route('/products')
def products():
    products_data =get_products()
    return render_template('products.html',products_data=products_data)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
    return redirect(url_for('products'))



@app.route('/sales', methods=['GET', 'POST'])
def sales():
    sales_data = get_sales()
    return render_template('sales.html',sales_data=sales_data)

@app.route('/add_sales', methods=['GET', 'POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']
        created_at = datetime.datetime.now()
        new_sale = [product_id, quantity,created_at]
        insert_sales(new_sale)
    return redirect(url_for('sales'))
    

@app.route('/stocks')
def stocks():
    stock_data=get_stocks()
    return render_template('stocks.html',stocks_data=stock_data)

@app.route('/add_stocks', methods=['GET', 'POST'])
def add_stocks():
    if request.method == 'POST':
        product_id = request.form['product_id']
        stock_quantity = request.form['quantity']
        created_at = datetime.datetime.now()
        new_stock = [product_id, stock_quantity,created_at]
        insert_sales(new_stock)
    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')







app.run(debug=True) #This starts the Flask server so your app is live and listening for visitors.