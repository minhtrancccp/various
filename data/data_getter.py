from dataclasses import dataclass
from enum import Enum
from os.path import abspath, dirname
from typing import Optional, TextIO


class SupportedFileTypes(Enum):
    html = ".html"
    txt = ".txt"


@dataclass
class FileKwargs:
    mode: str = "r"
    buffering: int = 1
    encoding: Optional[str] = None
    errors: Optional[str] = None
    newline: Optional[str] = None
    closefd: bool = True


def get_data(
    *relative_path: str,
    filetype: SupportedFileTypes = SupportedFileTypes.txt,
    kwargs: FileKwargs = FileKwargs()
) -> TextIO:
    data_root: str = dirname(abspath(__file__))
    return open(
        "\\".join((data_root, *relative_path)) + filetype.value, **kwargs.__dict__
    )


def main():
    print(*get_data("links"))


if __name__ == "__main__":
    main()
