from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class EXRWindow:
    x_min: int
    y_min: int
    x_max: int
    y_max: int

    @property
    def min(self) -> Tuple[int, int]:
        return (self.x_min, self.y_min)

    @property
    def max(self) -> Tuple[int, int]:
        return (self.x_max, self.y_max)

    @property
    def width(self) -> int:
        assert self.x_max > self.x_min
        return 1 + self.x_max - self.x_min

    @property
    def height(self) -> int:
        assert self.y_max > self.y_min
        return 1 + self.y_max - self.y_min

    @classmethod
    def parse_raw_to_window(cls, raw_window: Any):
        return EXRWindow(
            x_min=raw_window.min.x,
            y_min=raw_window.min.y,
            x_max=raw_window.max.x,
            y_max=raw_window.max.y,
        )
