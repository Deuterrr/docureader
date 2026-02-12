from abc import ABC, abstractmethod

from src.lib.domain.entities.image_entity import ImageEntity
from src.lib.domain.entities.detection_box_entity import DetectionBoxEntity


class ClassifierInterface(ABC):
    @abstractmethod
    def detect(
        self,
        image: ImageEntity,
        target_size: int = 640,
    ) -> tuple[list[DetectionBoxEntity], float]:
        """
        Run detection on image and return standardized results.
        """
        pass