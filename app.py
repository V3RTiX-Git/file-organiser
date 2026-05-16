from flask import Flask, render_template, request, jsonify
from organiser import organise_folder

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/organise", methods=["POST"])
def organise():
    data = request.get_json()
    folder_path = data.get("path", "").strip()
    result = organise_folder(folder_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)