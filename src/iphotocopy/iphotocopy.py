from pathlib import Path
import shutil
import logging
from typing import ClassVar
from PIL import Image, UnidentifiedImageError
from tqdm import tqdm  # Added for progress bar

logger = logging.getLogger(__name__)


class ApplePhotoCopier:
    """
    Copies or moves Apple photos from a source folder to a destination.
    """

    APPLE_EXTS: ClassVar[tuple[str, ...]] = (
        ".heic",
        ".heif",
        ".jpg",
        ".jpeg",
        ".png",
        ".tif",
        ".tiff",
        ".dng",
    )

    def __init__(
        self, source: Path, destination: Path, move: bool = False, dry_run: bool = False
    ):
        """
        Args:
            source (Path): Source directory.
            destination (Path): Destination directory.
            move (bool): If True, files are moved instead of copied.
            dry_run (bool): If True, simulate the action without changing files.
        """
        self.source: Path = source
        self.destination: Path = destination
        self.move: bool = move
        self.dry_run: bool = dry_run
        self.files_copied: int = 0

    def is_apple_image_file(self, filename: str) -> bool:
        """
        Returns True if filename has a known Apple photo extension.
        """
        return filename.lower().endswith(self.APPLE_EXTS)

    def get_exif_make(self, image_path: Path) -> str | None:
        """
        Reads EXIF ‘Make’ tag from image.

        Returns:
            str | None: the EXIF 'Make' value or None if unreadable.
        """
        try:
            with Image.open(image_path) as img:
                exif = img.getexif()
                if exif:
                    return exif.get(271)
        except (UnidentifiedImageError, OSError) as e:
            logger.warning(f"Could not read {image_path}: {e}")
        return None

    def prepare_destination(self) -> None:
        """
        Ensures source dir exists and destination dir is created if needed.
        """
        if not self.source.is_dir():
            raise FileNotFoundError(f"Source folder does not exist: {self.source}")
        try:
            self.destination.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise PermissionError(
                f"Could not create destination: {self.destination}\nReason: {e}"
            ) from e

    def copy(self) -> None:
        """
        Copies or moves Apple image files from source to destination.
        """
        self.prepare_destination()

        files = [
            f
            for f in self.source.iterdir()
            if f.is_file() and self.is_apple_image_file(f.name)
        ]

        for file in tqdm(files, desc="Processing images", unit="file"):
            make = self.get_exif_make(file)
            if make == "Apple":
                target = self.destination / file.name
                if self.dry_run:
                    logger.info(
                        f"[Dry-run] Would {'move' if self.move else 'copy'} {file.name} -> {target}"
                    )
                else:
                    logger.info(
                        f"{'Moving' if self.move else 'Copying'} {file.name} -> {target}"
                    )
                    try:
                        if self.move:
                            shutil.move(file, target)
                        else:
                            shutil.copy2(file, target)
                        self.files_copied += 1
                    except Exception as err:
                        logger.error(f"Error processing {file}: {err}")

        logger.info(
            f"Finished. {self.files_copied} Apple photo(s) {'moved' if self.move else 'copied'}."
            + (f" (Dry run)" if self.dry_run else "")
        )
