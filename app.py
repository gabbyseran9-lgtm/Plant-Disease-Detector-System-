from flask import Flask, render_template, request

app = Flask(__name__)

diseases = {
    "brown_spots": {
        "disease": "Leaf Spot",
        "description": "Brown or black spots appear on the leaves.",
        "treatment": "Remove affected leaves and avoid overwatering."
    },
    "yellow_leaves": {
        "disease": "Nutrient Deficiency",
        "description": "Leaves become yellow because the plant may lack nutrients.",
        "treatment": "Apply proper fertilizer and check soil condition."
    },
    "white_powder": {
        "disease": "Powdery Mildew",
        "description": "White powder-like patches appear on the leaves.",
        "treatment": "Remove infected leaves and improve air circulation."
    },
    "wilting": {
        "disease": "Possible Root Rot",
        "description": "The plant wilts even when the soil is wet.",
        "treatment": "Reduce watering and check the roots for damage."
    },
    "healthy": {
        "disease": "Healthy Plant",
        "description": "No obvious disease symptoms detected.",
        "treatment": "Continue proper watering and plant care."
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():
    plant = request.form.get("plant")
    symptom = request.form.get("symptom")

    result = diseases.get(symptom)

    if result:
        return render_template(
            "result.html",
            plant=plant,
            disease=result["disease"],
            description=result["description"],
            treatment=result["treatment"]
        )

    return "No result found."


if __name__ == "__main__":
    app.run(debug=True)
