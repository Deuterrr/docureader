from fastapi import FastAPI

from src.core.config import configs
from src.infra.models.yolo_model import YoloDetectionModel
from src.infra.services.yolo_detection_service import YoloDetectionService
from src.infra.services.image_processor_service import ImageProcessor
from src.lib.presentation.controllers.ktp_controller import KTPController
from src.lib.presentation.routes import web


def build_ktp_controller() -> KTPController:
    img_processor = ImageProcessor()

    card_classifier = YoloDetectionService(
        model=YoloDetectionModel(configs.KTP_DETECT_MODEL),
        image_processor=img_processor,
    )

    return KTPController(
        card_classifier=card_classifier,
    )


app = FastAPI(title="Hal-DocuReader")

ktp_controller = build_ktp_controller()
web.set_controller(ktp_controller)

app.include_router(web.router)
