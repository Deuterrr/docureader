from src.lib.domain.entities.image_entity import ImageEntity
from src.lib.domain.interfaces.classifier_interface import ClassifierInterface


class ClassifyKTPUseCase:
    def __init__(self, classifier):
        self.classifier: ClassifierInterface = classifier


    def execute(self, image: ImageEntity):
        ktp_results, elapsed = self.classifier.detect(image)

        if not ktp_results:
            raise ValueError("No KTP detected in the image.")

        expected_label = "ktp"
        min_conf = 0.7
        valid_results = [
            r for r in ktp_results
            if r.label.lower() == expected_label and r.confidence >= min_conf
        ]
        
        if not valid_results:
            raise ValueError(
                "Detected document is not a valid KTP.",
                elapsed
            )

        if len(valid_results) > 1:
            raise ValueError(
                f"Multiple KTP documents detected ({len(valid_results)}). "
                "Please upload one document at a time."
            )

        result = ktp_results[0]
        return {
            "doc_type": result.label,
            "confidence": result.confidence,
            "processing_time_ms": elapsed
        }