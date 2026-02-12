class YoloDetectionModel():
    def __init__(self, weight_path:str):
        from ultralytics import YOLO
        
        self.model = YOLO(weight_path)


    def predict(self, image):
        print("Initiate YOLO model detection ...")
        result = self.model.predict(image, verbose=False)[0]
        boxes = []
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = result.names[cls_id]
            boxes.append({
                "label": label,
                "bbox": box.xyxy[0].tolist(),
                "confidence": conf
            })
        return boxes