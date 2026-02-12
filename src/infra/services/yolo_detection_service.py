from src.lib.domain.entities.image_entity import ImageEntity
from src.lib.domain.entities.detection_box_entity import DetectionBoxEntity
from src.lib.domain.interfaces.classifier_interface import ClassifierInterface
from src.lib.domain.interfaces.image_processor_interface import ImageProcessorInterface


class YoloDetectionService(ClassifierInterface):
    def __init__(self, model, image_processor):
        import time

        self.time = time

        self.model = model
        self.img_processor: ImageProcessorInterface = image_processor

        
    def detect(self, image: ImageEntity, target_size=640) -> tuple[list[DetectionBoxEntity], float]:
        start = self.time.perf_counter()

        resized, scale, _ = self.img_processor.resize_keep_ratio(image, target_size)

        results = self.model.predict(resized.data)
        if not results:
            print("[WARNING] No object detected.")
            return [], 0

        mapped_results: list[DetectionBoxEntity] = []
        for r in results:
            bbox_resized = r["bbox"]
            bbox_ori = self.img_processor.map_bbox_to_original(bbox_resized, scale)

            mapped_results.append(
                DetectionBoxEntity(
                    label=r["label"],
                    bbox=[int(v) for v in bbox_ori],
                    confidence=round(r["confidence"], 3)
                )
            )

        elapsed: float = round((self.time.perf_counter() - start) * 1000, 2)
        return mapped_results, elapsed