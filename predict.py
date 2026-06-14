import os
import numpy as np
import cv2

# Load trained model
model = tf.keras.models.load_model("waste_classifier.keras")

# Alphabetical order of dataset subfolders — must match image_dataset_from_directory / train.py
def dataset_class_names(dataset_path="dataset"):
    if not os.path.isdir(dataset_path):
        raise FileNotFoundError(f"Missing '{dataset_path}/'")
    return sorted(
        d for d in os.listdir(dataset_path)
        if os.path.isdir(os.path.join(dataset_path, d))
    )

class_names = dataset_class_names()

# Load test image (BGR from file → RGB for model)
bgr = cv2.imread("test.jpg")   # change to your image name
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
img = cv2.resize(rgb, (224, 224))
img = img.astype(np.float32) / 255.0
img = np.expand_dims(img, axis=0)

# Predict
prediction = model.predict(img, verbose=0)
predicted_class = class_names[int(np.argmax(prediction))]

print("Predicted Waste Type:", predicted_class)
