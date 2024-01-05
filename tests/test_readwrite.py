from typing import Type
import numpy as np
import pytest
import openexr_python as exr
import os
import Imath

ASSET_DIR = os.path.join(os.path.dirname(__file__), "asset")


@pytest.mark.parametrize(
    [
        "file_path",
    ],
    [
        (os.path.join(ASSET_DIR, asset_name),)
        for asset_name in [
            "Balls.exr",
        ]
    ],
)
def test_read(file_path):
    input_file = exr.EXRInputFile(file_path=file_path)

    header = input_file.header
    channels = header.channels
    imgs = [input_file.read_numpy(c) for c in channels.keys()]
    size = exr.get_size_from_window(header.data_window)
    for img in imgs:
        h, w = img.shape
        assert (w, h) == size


def test_write():
    header = exr.EXRHeader.create_header(640, 480)
    for c in [
        "TestLayerRGBA.R",
        "TestLayerRGBA.G",
        "TestLayerRGBA.B",
        "TestLayerRGBA.A",
        "TestLayerRGB.R",
        "TestLayerRGB.G",
        "TestLayerRGB.B",
        "TestLayerR.R",
        "TestLayerGB.G",
        "TestLayerGB.B",
        "velocity.x",
        "velocity.y",
        "velocity.z",
        "depth.z",
        "adsad.x",
        "adsad.y",
        "adsad.z",
    ]:
        header.add_channel(c, exr.create_channel(np.float16))
    path = os.path.join(ASSET_DIR, "temp_openexr_for_test.exr")
    output_file = exr.EXROutputFile(file_path=path, header=header)
    pixels = {}
    for c_key in header.channels.keys():
        dtype = exr.convert_imath_type_to_numpy_type(header.channels[c_key].type)
        size = exr.get_size_from_window(header.data_window)
        numpy_buffer = np.zeros(shape=(size[1], size[0]), dtype=dtype)
        for j in range(size[1]):
            for i in range(size[0]):
                numpy_buffer[j, i] = (
                    1.0 * (i / size[0]) * (j / size[1]) * np.random.random()
                )
        pixels[c_key] = numpy_buffer
    output_file.write_pixels_with_numpy(pixels=pixels)
    assert os.path.exists(path=path)
    os.remove(path=path)
    assert not os.path.exists(path=path)
