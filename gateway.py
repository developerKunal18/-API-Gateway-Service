from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://127.0.0.1:5001"
ORDER_SERVICE = "http://127.0.0.1:5002"

# ---------- User Route ----------
@app.route("/api/users/<int:user_id>")
def get_user(user_id):

    response = requests.get(
        f"{USER_SERVICE}/users/{user_id}"
    )

    return jsonify(response.json())

# ---------- Order Route ----------
@app.route("/api/orders/<int:order_id>")
def get_order(order_id):

    response = requests.get(
        f"{ORDER_SERVICE}/orders/{order_id}"
    )

    return jsonify(response.json())

# ---------- Aggregated Route ----------
@app.route(
    "/api/user-order/<int:user_id>/<int:order_id>"
)
def user_order(user_id, order_id):

    user = requests.get(
        f"{USER_SERVICE}/users/{user_id}"
    ).json()

    order = requests.get(
        f"{ORDER_SERVICE}/orders/{order_id}"
    ).json()

    return jsonify({
        "user": user,
        "order": order
    })

if __name__ == "__main__":
    app.run(port=5000)
