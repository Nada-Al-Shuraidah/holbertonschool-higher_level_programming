from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if id_param:
        try:
            target_id = int(id_param)
            products = [p for p in products if p['id'] == target_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
