from dataclasses import dataclass
from typing import Any, Dict
import OpenEXR
import Imath


@dataclass
class EXRHeader:
    raw_header: Dict[str, Any]

    def __getitem__(self, key: str) -> Any:
        return self.raw_header[key]

    def add_channel(self, channel_name: str, channel_info: Imath.Channel):
        self.channels[channel_name] = channel_info

    def remove_channel(self, channel_name: str):
        self.channels.pop(channel_name)

    @property
    def channels(self) -> Dict[str, Imath.Channel]:
        raw_channels: Dict[str, Imath.Channel] = self["channels"]
        return raw_channels

    @property
    def compression(self) -> Imath.Compression:
        raw_compression: Imath.Compression = self["compression"]
        return raw_compression

    @property
    def data_window(self) -> Imath.Box2i:
        raw_dataWindow: Imath.Box2i = self["dataWindow"]
        return raw_dataWindow

    @property
    def display_window(self) -> Imath.Box2i:
        raw_dataWindow: Imath.Box2i = self["displayWindow"]
        return raw_dataWindow

    @property
    def line_order(self) -> Imath.LineOrder:
        raw_line_order: Imath.LineOrder = self["lineOrder"]
        return raw_line_order

    @property
    def pixel_aspect_ratio(self) -> float:
        raw_pixel_aspect_ratio: float = self["pixelAspectRatio"]
        return raw_pixel_aspect_ratio

    @property
    def screen_window_center(self) -> Imath.V2f:
        raw_screen_window_center: Imath.V2f = self["screenWindowCenter"]
        return raw_screen_window_center

    @property
    def screen_window_width(self) -> float:
        raw_screen_window_width: float = self["screenWindowWidth"]
        return raw_screen_window_width

    @classmethod
    def create_header(cls, width: int, height: int):
        raw_header = OpenEXR.Header(width, height)
        return EXRHeader(raw_header=raw_header)
