from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users/<int:user_id>")
def user(user_id):
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}"
    })

if __name__ == "__main__":
    app.run(port=5001)
