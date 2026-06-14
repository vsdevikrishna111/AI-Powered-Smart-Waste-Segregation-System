import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model("waste_classifier.keras")

# Create converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# 🔥 Optimization (IMPORTANT)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 🔥 ADD THIS LINE HERE
converter.target_spec.supported_types = [tf.float16]

# Convert model
tflite_model = converter.convert()

# Save model
with open("waste_classifier.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite model created successfully!")