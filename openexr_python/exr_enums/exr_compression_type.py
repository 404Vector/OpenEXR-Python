"""
ref : https://openexr.com/en/latest/OpenEXRFileLayout.html?highlight=xsampling#predefined-attribute-types
"""
from typing import Any
from openexr_python.exr_enums.exr_enum_base import EXREnumBase


class EXRCompressionType(EXREnumBase):
    Compression_NO = 0
    Compression_RLE = 1
    Compression_ZIPS = 2
    Compression_ZIP = 3
    Compression_PIZ = 4
    Compression_PXR24 = 5
    Compression_B44 = 6
    Compression_B44A = 7

    @classmethod
    def parse_raw2pyobj(cls, raw_compression: Any):
        return EXRCompressionType(value=raw_compression.v)
