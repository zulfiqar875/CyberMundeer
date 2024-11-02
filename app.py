from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")


@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Internal Server Error: {error}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
