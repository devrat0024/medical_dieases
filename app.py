from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load treatment data from JSON file
def load_treatment_data():
    with open("treatments.json", "r") as file:
        return json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_treatment", methods=["POST"])
def get_treatment():
    data = request.json
    cancer_type = data.get("cancerType", "").lower()
    cancer_stage = data.get("cancerStage", "")

    treatments = load_treatment_data()
    treatment = treatments.get(cancer_type, {}).get(cancer_stage, "No treatment found for this input.")

    return jsonify({"treatment": treatment})

if __name__ == "__main__":
    app.run(debug=True)
