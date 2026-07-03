from flask import Flask, jsonify

from config import VERSION
from database.health import check_database
from database.users import get_users, count_users

app = Flask(__name__)


@app.route("/api")
def api():
    return jsonify({
        "application": "Backend Running",
        "version": VERSION
    })


@app.route("/users")
def users():
    return jsonify(get_users())


@app.route("/health")
def health():
    return jsonify({
        "application": "UP",
        "database": check_database(),
        "users": count_users(),
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)