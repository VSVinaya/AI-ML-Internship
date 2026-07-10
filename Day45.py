# practical task
print("Load the YOLOv8 Model")
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
print("YOLOv8 model loaded successfully")

print("Run Object Detection")
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("image.jpg.jpg", save=True)
results[0].show()
print("Object detection completed successfully.")

