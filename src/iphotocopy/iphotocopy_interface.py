import logging
from pathlib import Path
from .iphotocopy_parser import build_parser
from .iphotocopy import ApplePhotoCopier


def main():
    """
    Interface entry point: parse CLI args, config logging, and run copier.
    """
    parser = build_parser()
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    copier = ApplePhotoCopier(
        Path(args.src_folder),
        Path(args.dest_folder),
        move=args.move,
        dry_run=args.dry_run,
    )
    copier.copy()
