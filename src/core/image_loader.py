from fastapi import UploadFile
import numpy as np
import cv2

from src.lib.domain.entities.image_entity import ImageEntity
from src.core.response_builder import APIResponse


async def load_image(file: UploadFile) -> ImageEntity:
    """
    Read an UploadFile and return a decoded cv2 image.
    Returns APIResponse.invalid_input if decoding fails.
    """
    try:
        image_bytes = await file.read()
        np_image = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        if image is None:
            return APIResponse.invalid_input("Invalid image format")
        
        return ImageEntity(data=image)
    except Exception as e:
        raise ValueError("File input cannot be executed")
