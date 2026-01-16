from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 允许任意跨域


@app.route("/api/time")
def time():
    return jsonify({"now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@app.route("/")
def home():
    return "<h1>Flask 运行正常</h1><p>请访问 <a href='/api/time'>/api/time</a></p>"


if __name__ == "__main__":
    app.run(debug=True)
