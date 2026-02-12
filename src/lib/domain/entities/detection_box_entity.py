from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class DetectionBoxEntity:
    confidence: float
    bbox: tuple[int, int, int, int]
    label: Optional[str] = None


    def __post_init__(self):
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError("confidence must be between 0 and 1")

        if len(self.bbox) != 4 or not all(isinstance(v, int) for v in self.bbox):
            raise ValueError("bbox must be 4 integers")