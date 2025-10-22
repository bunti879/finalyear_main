from flask import Blueprint, request, jsonify
import numpy as np
import os
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

api = Blueprint("api", __name__)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "crop_disease_model.h5")
LABELS_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "labels.json")

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    model = None

if os.path.exists(LABELS_PATH):
    with open(LABELS_PATH) as f:
        CLASS_LABELS = json.load(f)
else:
    CLASS_LABELS = { "0": "Healthy", "1": "Disease A", "2": "Disease B" }

@api.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    if model is None:
        return jsonify({"error": "Model not found"}), 500

    file = request.files["image"]
    img = image.load_img(file, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    confidence = float(np.max(preds))
    label = CLASS_LABELS[str(np.argmax(preds))]

    return jsonify({"label": label, "confidence": round(confidence, 3)})
