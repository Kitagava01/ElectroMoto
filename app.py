from flask import Flask, render_template, redirect, url_for, session
from products import products
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    else:
        return "Продукт не найден", 404

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
