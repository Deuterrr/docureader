from dataclasses import dataclass
from typing import Optional, Any


@dataclass(frozen=True)
class ImageEntity:
    data: Any
    width: Optional[int] = None
    height: Optional[int] = None
    color_space: str = "BGR"