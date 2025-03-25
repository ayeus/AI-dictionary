from flask import Flask, request, jsonify, send_from_directory
from dictionary_api import get_word_details
from user_data import save_progress, get_progress, get_history, save_bookmark, get_bookmarks
from daily_word import get_daily_word
from categories import get_category_words
from quiz_generator import generate_quiz, generate_passage, generate_puzzle
from utils.export_data import export_progress

app = Flask(__name__, static_folder="../frontend", static_url_path='')

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    print(f"Requesting: {path}")  # Debug log
    return send_from_directory(app.static_folder, path)

@app.route('/search_word', methods=['POST'])
def search_word():
    word = request.json['word']
    details = get_word_details(word)
    save_progress("user1", word)
    return jsonify(details)

@app.route('/daily_word', methods=['GET'])
def daily_word():
    word = get_daily_word()
    return jsonify(get_word_details(word))

@app.route('/categories/<level>', methods=['GET'])
def categories(level):
    words = get_category_words(level)
    return jsonify(words)

@app.route('/quiz', methods=['GET'])
def quiz():
    quiz_data = generate_quiz()
    return jsonify(quiz_data)

@app.route('/passage', methods=['GET'])
def passage():
    passage_data = generate_passage()
    return jsonify(passage_data)

@app.route('/puzzle', methods=['GET'])
def puzzle():
    puzzle_data = generate_puzzle()
    return jsonify(puzzle_data)

@app.route('/progress', methods=['GET'])
def progress():
    return jsonify(get_progress("user1"))

@app.route('/history', methods=['GET'])
def history():
    return jsonify(get_history("user1"))

@app.route('/bookmark', methods=['POST'])
def bookmark():
    word = request.json['word']
    save_bookmark("user1", word)
    return jsonify({"message": f"{word} bookmarked"})

@app.route('/bookmarks', methods=['GET'])
def bookmarks():
    return jsonify(get_bookmarks("user1"))

@app.route('/export_progress', methods=['GET'])
def export():
    file_path = export_progress("user1")
    return send_from_directory('.', file_path)

if __name__ == '__main__':
    app.run(debug=True)