from os.path import abspath, dirname

from typing import TextIO

# This is the project root
_ROOT_DIR = dirname(abspath(__file__))


def get_data(*relative_path: str) -> TextIO:
    return open("\\".join((_ROOT_DIR, "data") + relative_path), "a")
