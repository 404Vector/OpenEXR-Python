from dataclasses import dataclass
from typing import Any, Type
from openexr_python.exr_enums.exr_image_data_type import EXRImageDataType
from openexr_python.exr_channel_sampling_rate import EXRChannelSamplingRate


@dataclass
class EXRChannelInfo:
    data_type: Type[EXRImageDataType]
    sampling_rate: EXRChannelSamplingRate

    @classmethod
    def parse_raw2pyobj(cls, raw_channel_info: Any):
        return EXRChannelInfo(
            data_type=EXRImageDataType.parse_raw2pyobj(
                raw_channel_info=raw_channel_info,
            ),
            sampling_rate=EXRChannelSamplingRate.parse_raw2pyobj(
                raw_channel_info=raw_channel_info,
            ),
        )
