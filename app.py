from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


def extract_features(password):
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if not c.isalnum())

    return [[length, uppercase, lowercase, digits, special]]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    password = data["password"]

    features = extract_features(password)

    prediction = model.predict(features)[0]

    return jsonify({"strength": prediction})


if __name__ == "__main__":
    app.run(debug=True)