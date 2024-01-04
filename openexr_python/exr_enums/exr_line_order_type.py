"""
ref : https://openexr.com/en/latest/OpenEXRFileLayout.html?highlight=xsampling#predefined-attribute-types
"""
from openexr_python.exr_enums.exr_enum_base import EXREnumBase
from typing import Any


class EXRLineOrderType(EXREnumBase):
    Increasing_Y = 0
    Decreasing_Y = 1
    Random_Y = 2

    @classmethod
    def parse_raw2pyobj(cls, raw_line_order: Any):
        return EXRLineOrderType(value=raw_line_order.v)
