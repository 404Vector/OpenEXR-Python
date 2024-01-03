import argparse
import os
import datetime
import build

TAG_ENV_NAME = "GITHUB_ACTION_TAG_NAME"
VERSION_TEXT = "0.0.0"
PROJECT_DIR = os.path.dirname(__file__)
VERSION_FILE_PATH = os.path.join("openexr_python", "__init__.py")


def parse_args():
    paser = argparse.ArgumentParser()
    paser.add_argument("--debug", type=bool, action=argparse.BooleanOptionalAction)

    return paser.parse_args()


def get_version() -> str:
    if TAG_ENV_NAME in os.environ:
        return os.environ[TAG_ENV_NAME]
    else:
        return f"{datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y.%m.%d.%H.%M.%S')}"


def swap_version_with_tag(
    file_path: str,
    version_text: str,
    is_debug: bool,
):
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    version = get_version()
    if is_debug is True:
        print(
            f"The generated version is [{version}]. But swapping to [{version_text}] because this is debug mode."
        )
        version = version_text
    with open(file=file_path, mode="r") as f:
        file_text = str(f.read())
    assert file_text.find(version_text) > -1
    print(f"Build Version : {version}")
    file_text = file_text.replace(version_text, version)
    if is_debug is not True:
        assert file_text.find(version_text) == -1
    with open(file=file_path, mode="w") as f:
        result = f.write(file_text)
        print(result)


def build_package(is_debug: bool):
    if is_debug is not True:
        res = os.system("pip install build")
        assert res == 0, f"The building process failed. code = {res}"
    res = os.system("python -m build")
    assert res == 0, f"The building process failed. code = {res}"


def main(args: argparse.Namespace):
    is_debug: bool = args.debug

    swap_version_with_tag(
        file_path=VERSION_FILE_PATH,
        version_text=VERSION_TEXT,
        is_debug=is_debug,
    )
    build_package(
        is_debug=is_debug,
    )


if __name__ == "__main__":
    main(args=parse_args())
