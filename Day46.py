# practical task

print("Run Object Detection on an Image")
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("car.jpg.jpg", save=True)
results[0].show()

print("Different Confidence Values")
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
# Confidence = 0.3
model.predict("car.jpg.jpg", conf=0.3)
# Confidence = 0.5
model.predict("car.jpg.jpg", conf=0.5)
# Confidence = 0.8
model.predict("car.jpg.jpg", conf=0.8)

print("Print result.boxes")
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("car.jpg.jpg")
for result in results:
    print(result.boxes)
