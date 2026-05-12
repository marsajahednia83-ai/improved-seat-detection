from ultralytics import YOLO

model = YOLO('yolov8m.pt')  # changed from yolov8n to yolov8m

model.train(
    data='/content/drive/MyDrive/seat-detection2/data.yaml',
    epochs=50,
    imgsz=640,
    batch=8,        
    device=0,      
    name='seat_detector_v2'
)
