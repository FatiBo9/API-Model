from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model=tf.keras.models.load_model(r"C:\Users\PC\Desktop\software integration\cat\cats_vs_dogs.h5")

h= model.input_shape[1]
w= model.input_shape[2]
image_size=(w, h)  

def prepare_image(image: Image.Image):
    image=image.resize(image_size)
    array= np.array(image).astype(np.float32)/ 255.0
    array=np.expand_dims(array, axis=0)
    return array

def predict_label(processed_image):
    pred= model.predict(processed_image)
    pred= np.array(pred)

    if pred.size== 1:
        score= float(pred.reshape(-1)[0])
        label= "dog" if score > 0.5 else "cat"
        return label, score

    if pred.shape[-1]== 2:
        pred_class= int(np.argmax(pred, axis=-1)[0])
        score= float(np.max(pred, axis=-1)[0])
        label ="cat" if pred_class == 0 else "dog"
        return label, score

    return "unknown image ", None

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided, please upload a file"}), 400

    file=request.files["file"]
    try:
        image=Image.open(io.BytesIO(file.read())).convert("RGB")
    except Exception as e:
        return jsonify({"error": f"Uploaded file is not a valid image: {str(e)}"}), 400

    processed=prepare_image(image)
    label, score= predict_label(processed)

    return jsonify({"label": label, "score": score, "model_input_size": [w, h]})

@app.route("/predict-batch", methods=["POST"])
def predict_batch():
    files = request.files.getlist("files")

    if not files:
        return jsonify({"error": "No file provided, please upload a file"}), 400
    results = []

    for file in files:
        try:
            image= Image.open(io.BytesIO(file.read())).convert("RGB")
            processed= prepare_image(image)
            label, _= predict_label(processed) 

            results.append({
                "filename": file.filename,
                "label": label
            })

        except Exception as e:
            results.append({
                "filename": file.filename,
                "label": "error"
            })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)