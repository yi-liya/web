from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/api/time")
def time():
    return jsonify({"now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))