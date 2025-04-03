from flask import Flask, request, jsonify, render_template
from bug_fixer import detect_and_fix_bug

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fix_bug", methods=["POST"])
def fix_bug():
    data = request.json
    language = data.get("language", "").strip()
    code = data.get("code", "").strip()

    if not language or not code:
        return jsonify({"error": "Please select a language and enter code"}), 400

    result = detect_and_fix_bug(language, code)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
