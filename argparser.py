import argparse
import pathlib
import os


def resolved_path(path):
    return os.path.realpath(os.path.normpath(os.path.expanduser(path)))


def parse_args():
    parser = argparse.ArgumentParser(
        description="This script will request all jobs listed at your air table and render images based on them"
    )

    parser.add_argument(
        "key",
        help="Your Air Tables API Key",
        type=str,
    )
    parser.add_argument(
        "app",
        help="You Air Tables APP ID",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--all-images",
        help="Ignore the Imagem column and process every line",
        action="store_true"
    )
    parser.add_argument(
        "-b",
        "--background-image",
        help="What background image should be used",
        choices=["random", "purple", "black"],
        default="random",
        type=str
    )
    parser.add_argument(
        "-o",
        "--output-directory",
        help="Images output folder",
        default="output/",
        type=resolved_path
    )

    return parser.parse_args()
