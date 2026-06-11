from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders/<int:order_id>")
def order(order_id):
    return jsonify({
        "id": order_id,
        "product": "Laptop"
    })

if __name__ == "__main__":
    app.run(port=5002)
