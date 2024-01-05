from typing import Tuple
import Imath
import numpy as np

PIXEL_TYPE_CONVERT_MAP = {
    np.uint32: Imath.PixelType.UINT,
    np.float16: Imath.PixelType.HALF,
    np.float32: Imath.PixelType.FLOAT,
    Imath.PixelType.UINT: np.uint32,
    Imath.PixelType.HALF: np.float16,
    Imath.PixelType.FLOAT: np.float32,
}


def convert_numpy_type_to_imath_type(data_type: np.dtype) -> Imath.PixelType:
    assert data_type in [np.float16, np.float32, np.uint32]
    keys = [k for k in PIXEL_TYPE_CONVERT_MAP.keys()]
    idx = -1
    for i, key in enumerate(keys):
        if key != data_type:
            continue
        idx = i
        break
    assert idx != -1
    return Imath.PixelType(PIXEL_TYPE_CONVERT_MAP[keys[idx]])


def convert_imath_type_to_numpy_type(data_type: Imath.PixelType):
    assert type(data_type) is Imath.PixelType
    assert data_type.v in PIXEL_TYPE_CONVERT_MAP
    return PIXEL_TYPE_CONVERT_MAP[data_type.v]


def create_channel(data_type: np.dtype, sampling_x: int = 1, sampling_y: int = 1):
    assert sampling_x > 0
    assert sampling_y > 0
    im_data_type = convert_numpy_type_to_imath_type(data_type)
    return Imath.Channel(type=im_data_type, xSampling=1, ySampling=1)


def get_size_from_window(window: Imath.Box2i) -> Tuple[int, int]:
    return (1 + window.max.x - window.min.x, 1 + window.max.y - window.min.y)
