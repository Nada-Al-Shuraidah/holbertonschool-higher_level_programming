from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    items_list = []

    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception as e:
        print(f"Error reading items.json: {e}")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
