from flask import Flask, request, jsonify

app = Flask(__name__)


def is_square_matrix(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0:
        return False
    n = len(matrix)
    return all(isinstance(row, list) and len(row) == n for row in matrix)


def add_matrices(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def transpose_matrix(a):
    n = len(a)
    return [[a[j][i] for j in range(n)] for i in range(n)]


def multiply_matrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Matrix API is running"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    }), 200


@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()

    if not data or "matrix1" not in data or "matrix2" not in data:
        return jsonify({"error": "Request must contain matrix1 and matrix2"}), 400

    matrix1 = data["matrix1"]
    matrix2 = data["matrix2"]

    if not is_square_matrix(matrix1) or not is_square_matrix(matrix2):
        return jsonify({"error": "Both inputs must be square matrices"}), 400

    if len(matrix1) != len(matrix2):
        return jsonify({"error": "Matrices must be the same size"}), 400

    result = add_matrices(matrix1, matrix2)
    return jsonify({"result": result}), 200


@app.route("/api/transpose", methods=["POST"])
def transpose():
    data = request.get_json()

    if not data or "matrix" not in data:
        return jsonify({"error": "Request must contain matrix"}), 400

    matrix = data["matrix"]

    if not is_square_matrix(matrix):
        return jsonify({"error": "Input must be a square matrix"}), 400

    result = transpose_matrix(matrix)
    return jsonify({"result": result}), 200


@app.route("/api/multiply", methods=["POST"])
def multiply():
    data = request.get_json()

    if not data or "matrix1" not in data or "matrix2" not in data:
        return jsonify({"error": "Request must contain matrix1 and matrix2"}), 400

    matrix1 = data["matrix1"]
    matrix2 = data["matrix2"]

    if not is_square_matrix(matrix1) or not is_square_matrix(matrix2):
        return jsonify({"error": "Both inputs must be square matrices"}), 400

    if len(matrix1) != len(matrix2):
        return jsonify({"error": "Matrices must be the same size"}), 400

    result = multiply_matrices(matrix1, matrix2)
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)