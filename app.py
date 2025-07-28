from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')  

@app.route('/style.css')
def style():
    return send_file('style.css')  

@app.route('/', methods=['POST'])
def predict():
  
    product = request.form['product']
    category = request.form['category']
    quantity = float(request.form['quantity'])
    price = float(request.form['price'])
    rating = float(request.form['rating'])
    delivery_time = float(request.form['delivery_time'])

    # Dummy prediction
    revenue = quantity * price * (1 + rating / 10) - delivery_time * 5

    # Return HTML string as response
    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Sales Forecast</h1>
            <h2>Predicted Revenue: ₹ {revenue:.2f}</h2>
            <a href="/">Back</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
