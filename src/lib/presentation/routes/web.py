from fastapi import APIRouter, UploadFile, File

from src.core.file_checker import validate_image_file
from src.lib.presentation.controllers.ktp_controller import KTPController

router = APIRouter(tags=["documents"])

_controller: KTPController | None = None


def set_controller(controller: KTPController):
    global _controller
    _controller = controller


@router.post("/ktp/classify")
async def classify_ktp(
    file: UploadFile = File(...),
):
    await validate_image_file(file)
    return await _controller.classify(file)