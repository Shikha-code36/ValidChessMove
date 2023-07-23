from flask import Flask, request, jsonify
from chess_moves import Rook, Queen, Bishop, Knight

app = Flask(__name__)

@app.route('/chess/<slug>', methods=['POST'])
def get_valid_moves(slug):
    data = request.get_json()
    positions = data.get("positions", {})
    slug =slug.capitalize()

    position = positions.get(slug)
    if not position:
        return jsonify({"error": f"Position not provided for {slug}."}), 400

    piece_map = {
        "rook": Rook,
        "queen": Queen,
        "bishop": Bishop,
        "knight": Knight
    }

    slug_lower = slug.lower()
    if slug_lower not in piece_map:
        return jsonify({"error": f"Invalid chess piece: {slug}"}), 400

    piece = piece_map[slug_lower](position)
    valid_moves = piece.get_valid_moves()

    return jsonify({"valid_moves": valid_moves})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
