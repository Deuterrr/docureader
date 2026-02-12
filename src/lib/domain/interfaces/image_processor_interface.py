from abc import ABC, abstractmethod

from src.lib.domain.entities.image_entity import ImageEntity


class ImageProcessorInterface(ABC):
    @abstractmethod
    def resize_keep_ratio(self, image: ImageEntity, target_size: int) -> tuple[ImageEntity, float, tuple[int, int]]:
        """
        Resize image while keeping aspect ratio.
        Returns resized image, scale factor, and original shape.
        """
        pass


    @abstractmethod
    def map_bbox_to_original(self, bbox_resized, scale) -> list[int]:
        """
        Map bbox from resized coordinates back to original image size.
        """
        pass