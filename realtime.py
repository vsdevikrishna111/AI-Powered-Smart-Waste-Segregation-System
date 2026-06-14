import cv2
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("waste_classifier.keras")

# Class labels (must match training folder names)
class_names = ["dry", "recyclable", "wet"]

# Start webcam
cap = cv2.VideoCapture(0)

# 🔹 ADD THIS before loop (for smoothing)
predictions_list = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to model input size
    img = cv2.resize(frame, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # 🔹 MODEL PREDICTION
    prediction = model.predict(img, verbose=0)[0]

    # 🔹 ADD prediction to list
    predictions_list.append(prediction)

    # Keep last 10 frames only
    if len(predictions_list) > 10:
        predictions_list.pop(0)

    # 🔹 TAKE AVERAGE (SMOOTHING)
    avg_prediction = np.mean(predictions_list, axis=0)

    predicted_class = class_names[np.argmax(avg_prediction)]
    confidence = np.max(avg_prediction)

    # 🔹 Apply confidence threshold
    if confidence > 0.70:
        label = f"{predicted_class} ({confidence*100:.1f}%)"
    else:
        label = "Detecting..."

    # Display result on screen
    cv2.putText(frame, label, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow("Waste Classifier", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()