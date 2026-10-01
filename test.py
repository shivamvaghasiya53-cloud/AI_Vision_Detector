from detect import detect_objects
import cv2

image, counts = detect_objects("uploads/image.jpeg")   # Change image name if needed

# Resize image for display
height, width = image.shape[:2]

max_width = 1000
max_height = 700

scale = min(max_width / width, max_height / height)

new_width = int(width * scale)
new_height = int(height * scale)

resized = cv2.resize(image, (new_width, new_height))

cv2.imshow("Detected Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nDetected Objects:")
for name, count in counts.items():
    print(f"{name}: {count}")