from flask import Flask, request

app = Flask(__name__)

# Business Logic
def calculate_discount(price):
    if price > 1000:
        return price * 0.9   # 10% discount
    return price

# UI + Backend (Route)
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    
    if request.method == "POST":
        try:
            price = float(request.form["price"])
            final_price = calculate_discount(price)
            result = f"Final Price after discount: {final_price}"
        except:
            result = "Invalid input"

    return f"""
    <html>
        <head>
            <title>Monolithic Python App</title>
        </head>
        <body>
            <h2>Price Calculator</h2>
            <form method="post">
                Enter Price: <input type="text" name="price" />
                <input type="submit" value="Calculate" />
            </form>
            <p>{result}</p>
        </body>
    </html>
    """

# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
