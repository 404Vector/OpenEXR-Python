from dataclasses import dataclass
from typing import Any, Dict, Tuple
from openexr_python.exr_enums import EXRCompressionType, EXRLineOrderType
from openexr_python.exr_channel_info import EXRChannelInfo
from openexr_python.exr_window import EXRWindow


@dataclass
class EXRHeader:
    _header_raw_dict: Dict[str, Any]

    def __getitem__(self, key: str) -> Any:
        return self._header_raw_dict[key]

    @property
    def channels(self) -> Dict[str, EXRChannelInfo]:
        raw_channels: Dict[str, Any] = self["channels"]
        return {
            key: EXRChannelInfo.parse_raw2pyobj(raw_channel_info=value)
            for key, value in raw_channels.items()
        }

    @property
    def compression(self) -> EXRCompressionType:
        raw_compression: Any = self["compression"]
        return EXRCompressionType.parse_raw2pyobj(raw_compression=raw_compression)

    @property
    def data_window(self) -> EXRWindow:
        raw_dataWindow: Any = self["dataWindow"]
        return EXRWindow.parse_raw_to_window(raw_dataWindow)

    @property
    def display_window(self) -> EXRWindow:
        raw_dataWindow: Any = self["displayWindow"]
        return EXRWindow.parse_raw_to_window(raw_dataWindow)

    @property
    def line_order(self) -> EXRLineOrderType:
        raw_line_order: Any = self["lineOrder"]
        return EXRLineOrderType.parse_raw2pyobj(raw_line_order=raw_line_order)

    @property
    def pixel_aspect_ratio(self) -> float:
        raw_pixel_aspect_ratio: float = self["pixelAspectRatio"]
        return raw_pixel_aspect_ratio

    @property
    def screen_window_center(self) -> Tuple[float, float]:
        raw_screen_window_center: Any = self["screenWindowCenter"]
        return (raw_screen_window_center.x, raw_screen_window_center.y)

    @property
    def screen_window_width(self) -> float:
        raw_screen_window_width: float = self["screenWindowWidth"]
        return raw_screen_window_width
