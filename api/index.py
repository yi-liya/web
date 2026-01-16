from flask import Flask, jsonify
from flask_cors import CORS  # 允许任意跨域
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/api/time")
def time():
    return jsonify({"now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})