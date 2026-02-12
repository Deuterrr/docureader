import numpy as np
import cv2

from src.lib.domain.interfaces.image_processor_interface import ImageProcessorInterface
from src.lib.domain.entities.image_entity import ImageEntity


class ImageProcessor(ImageProcessorInterface):
    def resize_keep_ratio(self, img: ImageEntity, target_size) -> tuple[ImageEntity, float, tuple[int, int]]:
        image = img.data
        
        orig_h, orig_w = image.shape[:2]
        scale = target_size / max(orig_h, orig_w)
        new_w, new_h = int(orig_w * scale), int(orig_h * scale)

        if not isinstance(image, np.ndarray):
            raise TypeError(f"impl got type: {type(image)}")

        resized = cv2.resize(image, (new_w, new_h))
        return ImageEntity(data=resized), scale, (orig_h, orig_w)
    

    def map_bbox_to_original(self, bbox, scale) -> list[int]:
        x1, y1, x2, y2 = bbox
        return [
            int(round(x1 / scale)),
            int(round(y1 / scale)),
            int(round(x2 / scale)),
            int(round(y2 / scale)),
        ]