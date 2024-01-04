"""
ref : https://openexr.com/en/latest/OpenEXRFileLayout.html?highlight=xsampling#predefined-attribute-types
"""
from openexr_python.exr_enums.exr_enum_base import EXREnumBase
from typing import Any


class EXRImageDataType(EXREnumBase):
    UINT32 = 0
    FLOAT16 = 1
    FLOAT32 = 2

    @classmethod
    def parse_raw2pyobj(cls, raw_channel_info: Any):
        return EXRImageDataType(value=raw_channel_info.type.v)
