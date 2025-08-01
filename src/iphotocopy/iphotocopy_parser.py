import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    Builds an ArgumentParser for the iphotocopy tool.

    Returns:
        argparse.ArgumentParser: configured parser with source, destination, move and dry-run args.
    """
    parser = argparse.ArgumentParser(
        description="Filter and copy Apple iPhone photos from one directory to another."
    )
    parser.add_argument(
        "-i",
        "--src_folder",
        required=True,
        type=str,
        help="source directory path",
    )
    parser.add_argument(
        "-o",
        "--dest_folder",
        required=True,
        type=str,
        help="destination directory path",
    )
    parser.add_argument(
        "-m",
        "--move",
        action="store_true",
        help="move files instead of copying them",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without performing them (no files will be copied or moved)",
    )

    return parser
