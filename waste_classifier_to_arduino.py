import cv2
import tensorflow as tf
import serial
import time
import numpy as np

# ---------- Serial ----------
arduino = serial.Serial('COM11', 9600)
time.sleep(2)

# ---------- Model ----------
model = tf.keras.models.load_model("waste_classifier.keras")
class_names = ["dry", "wet", "recycle"]

# ---------- Camera ----------
cap = cv2.VideoCapture(0)

print("Press 'c' to detect | 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow("Waste Classifier", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):

        img = cv2.resize(frame, (224, 224))
        img = img / 255.0
        img = img.reshape(1, 224, 224, 3)

        prediction = model.predict(img)
        class_index = np.argmax(prediction)
        confidence = np.max(prediction)

        #print(f"Detected: {class_names[class_index]} ({confidence:.2f})")
        result = class_names[class_index]
        #print("result is: ",result)
        print(type(result))
        if confidence > 0.7:
            print("Place waste in front of IR sensor...")
            time.sleep(2)
            result = class_names[class_index]
            result = result + "\n"
            arduino.write(result.encode())
            print("result is",result)
            print("Sent to Arduino",result)

            time.sleep(5)  # wait for system

        else:
            print("Low confidence")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()