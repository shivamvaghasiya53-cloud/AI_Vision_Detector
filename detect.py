from ultralytics import YOLO
from collections import Counter
import cv2

# Load YOLO model only once
model = YOLO("yolov8n.pt")


def detect_objects(image_path):
    results = model(image_path)

    result = results[0]

    # Draw bounding boxes
    annotated_image = result.plot()

    detected_objects = []

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        detected_objects.append(class_name)

    counts = Counter(detected_objects)

    return annotated_image, counts