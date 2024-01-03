# OpenEXR-Python

[OpenEXR](https://github.com/AcademySoftwareFoundation/openexr) is a C++-based library, and there is a python binding ([pip-openexr](https://github.com/sanguinariojoe/pip-openexr?tab=readme-ov-file)) written by 'sanguinariojoe'.

However, because it was bound directly, python intellisense does not work.

For the convenience of development in the Python environment, this library wraps sanguinariojoe's Python binding into Python once again to support intellisense.

## [OpenEXR](https://github.com/AcademySoftwareFoundation/openexr)

OpenEXR provides the specification and reference implementation of the EXR file format, the professional-grade image storage format of the motion picture industry.

The purpose of EXR format is to accurately and efficiently represent high-dynamic-range scene-linear image data and associated metadata, with strong support for multi-part, multi-channel use cases.

OpenEXR is widely used in host application software where accuracy is critical, such as photorealistic rendering, texture access, image compositing, deep compositing, and DI.

## Installation

### Step 1 - Install OpenEXR
Please install following the [official installation guide](https://openexr.com/en/latest/install.html).

### Step 2 - Install OpenEXR-Python
```bash
pip install openexr-python
```
