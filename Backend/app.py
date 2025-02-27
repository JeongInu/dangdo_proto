from flask import Flask, jsonify
from flask_cors import CORS

# Flask 생성
app = Flask(__name__)
app.config.from_object(__name__)

# CORS 설정 -> 서버/클라이언트 다른 도메인에서 실행될 때 발생하는 차단 문제 방지
CORS(app, resources={r"/*": {"origins": "*"}})

# Sanity Check
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong~!')

if __name__ == '__main__':
    app.run(debug=True)