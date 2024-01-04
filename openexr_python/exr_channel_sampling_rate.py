from dataclasses import dataclass
from typing import Any


@dataclass
class EXRChannelSamplingRate:
    x_sampling: int
    y_sampling: int

    @classmethod
    def parse_raw2pyobj(cls, raw_channel_info: Any):
        return EXRChannelSamplingRate(
            x_sampling=raw_channel_info.xSampling, y_sampling=raw_channel_info.ySampling
        )
