from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# -----------------------------
# Load ML Model + Label Encoder.
# -----------------------------
MODEL_PATH = "C:\\Users\\Chetan\\OneDrive\\Desktop\\crop\\Models\\crop_recommendation\\crop_label_encoder.joblib"
ENCODER_PATH ="C:\\Users\\Chetan\\OneDrive\\Desktop\\crop\\Models\\crop_recommendation\\crop_recommender_model.joblib"

crop_model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/recommend-crop", methods=["POST"])
def recommend_crop():
    try:
        data = request.get_json()

        features = np.array([[
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temp']),
            float(data['humidity']),
            float(data['pH']),
            float(data['rainfall'])
        ]])

        prediction = crop_model.predict(features)[0]
        confidence = np.max(crop_model.predict_proba(features)) * 100

        crop_name = label_encoder.inverse_transform([prediction])[0]

        return jsonify({
            "recommended_crop": crop_name,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
