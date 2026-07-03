from flask import Flask, jsonify, render_template
from database import check_database
from config import VERSION

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        version=VERSION
    )


@app.route("/api")
def api():
    return jsonify({
        "application": "Backend Running",
        "version": VERSION
    })


@app.route("/health")
def health():

    db_status = check_database()

    return jsonify({
        "application": "UP",
        "database": db_status,
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
