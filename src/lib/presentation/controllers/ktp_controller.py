from src.core.image_loader import load_image
from src.core.response_builder import APIResponse
from src.lib.app.usecases.classify_ktp_usecase import ClassifyKTPUseCase


class KTPController:
    def __init__(
            self,
            card_classifier,
        ):
        self.card_classifier = card_classifier


    async def classify(self, ktp):
        try:
            image = await load_image(ktp)
            usecase = ClassifyKTPUseCase(self.card_classifier)
            data = usecase.execute(image)
            return APIResponse.success(data)
        except ValueError as e:
            return APIResponse.invalid_input(str(e))
        except FileNotFoundError:
            return APIResponse.data_not_found()
        except Exception as e:
            print("Unhandled error:", e)
            return APIResponse.internal_error(str(e))