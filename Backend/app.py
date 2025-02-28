from flask import Flask, jsonify, request
from flask_cors import CORS

# Flask 생성
app = Flask(__name__)
app.config.from_object(__name__)

# CORS 설정 -> 서버/클라이언트 다른 도메인에서 실행될 때 발생하는 차단 문제 방지
CORS(app, resources={r"/*": {"origins": "*"}})

BOOKS = [
    {
        'title': '문학의 숲을 거닐다',
        'author': '장영희',
        'read': True,
        'sweet': 1
    },
    {
        'title': '천년을 훔치다',
        'author': '조완선',
        'read': False,
        'sweet': 0
    },
    {
        'title': '칼의 노래',
        'author': '김훈',
        'read': True,
        'sweet': 2
    }
]

# Sanity Check
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong~!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'sweet': post_data.get('sweet')
        })

        response_object['message'] = '도서 추가!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)
