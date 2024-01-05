from dataclasses import dataclass
import os
from typing import Any, Dict, List, Tuple

import numpy as np
from openexr_python.exr_header import EXRHeader
import OpenEXR
from openexr_python.util import (
    get_size_from_window,
    convert_numpy_type_to_imath_type,
    convert_imath_type_to_numpy_type,
)


class EXROutputFile:
    def __init__(self, file_path: str, header: EXRHeader) -> None:
        assert os.path.isdir(os.path.dirname(file_path))
        self.file_path = file_path
        self.header = header
        self.raw_output_file: Any = OpenEXR.OutputFile(file_path, header.raw_header)
        self._is_closed = False

    def write_pixels(self, pixels: Dict[str, bytes]):
        assert self._is_closed is not True, f"The EXR File already has been closed."
        self.raw_output_file.writePixels(pixels)
        self._close()

    def _convert_bytes_to_numpy(self, numpy_buffer: np.ndarray):
        # check the buffer is 2 dim shape(h x w)
        shape = numpy_buffer.shape
        assert len(shape) == 2
        # check the buffer is fit to the window size
        data_height, data_width = shape
        window_width, window_height = get_size_from_window(self.header.data_window)
        assert window_width == data_width
        assert window_height == data_height
        return numpy_buffer.tobytes()

    def write_pixels_with_numpy(self, pixels: Dict[str, np.ndarray]):
        pixels_bytes: Dict[str, bytes] = {}
        for channel_name, numpy_buffer in pixels.items():
            # check the channel is exist
            assert channel_name in self.header.channels
            pixels_bytes[channel_name] = self._convert_bytes_to_numpy(
                numpy_buffer=numpy_buffer
            )
            # check the buffer type is fit to the window type
            assert (
                convert_numpy_type_to_imath_type(numpy_buffer.dtype)
                == self.header.channels[channel_name].type
            )
        self.write_pixels(pixels=pixels_bytes)

    def current_scan_line(self):
        return self.raw_output_file.currentScanLine()

    def _close(self):
        assert self._is_closed is not True, f"The EXR File already has been closed."
        self.raw_output_file.close()
        self._is_closed = True
