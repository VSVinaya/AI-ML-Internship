# print("Run Detection on a Video File")
# import cv2
# from ultralytics import YOLO
# model = YOLO("yolov8n.pt")
# video = cv2.VideoCapture("dog.mp4.mp4")
# while True:
#     success, frame = video.read()
#     if not success:
#         break
#     results = model(frame)
#     annotated_frame = results[0].plot()
#     cv2.imshow("YOLO Video Detection", annotated_frame)
#     if cv2.waitKey(1) == 27:
#         break
# video.release()
# cv2.destroyAllWindows()
 

print("Run Real-Time Webcam Detection")
import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    if not success:
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Live Detection", annotated_frame)
    if cv2.waitKey(1) == 27:
        break
camera.release()
cv2.destroyAllWindows()
