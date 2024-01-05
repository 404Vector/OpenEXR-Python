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


class EXRInputFile:
    def __init__(self, file_path: str):
        assert OpenEXR.isOpenExrFile(file_path)
        self.file_path = file_path
        self.raw_input_file: Any = OpenEXR.InputFile(file_path)

    def get_single_channel_buffer(self, channel_key: str) -> bytes:
        return self.raw_input_file.channel(channel_key)

    def get_multi_channel_buffer(self, channel_keys: List[str]) -> List[bytes]:
        assert len(channel_keys) > 0
        assert all([len(c) == 1 for c in channel_keys])
        return self.raw_input_file.channels(channel_keys)

    def read_numpy(self, channel_key: str) -> np.ndarray:
        header = self.header
        buffer = self.get_single_channel_buffer(channel_key=channel_key)
        channel_info = header.channels[channel_key]
        dtype = convert_imath_type_to_numpy_type(channel_info.type)
        np_buffer = np.frombuffer(buffer=buffer, dtype=dtype)
        size = get_size_from_window(header.data_window)
        return np.reshape(np_buffer, newshape=(size[1], size[0]))

    def close(self):
        self.raw_input_file.close()

    @property
    def header(self) -> EXRHeader:
        raw_header = self.raw_input_file.header()
        return EXRHeader(raw_header=raw_header)

    @property
    def is_complete(self) -> bool:
        """
        Returns whether this exr file contains all data and is not missing.

        Returns:
            bool
        """
        return self.raw_input_file.isComplete()
