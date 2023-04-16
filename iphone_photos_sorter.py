import logging
from pathlib import Path
from PIL import Image
import shutil

class AppleImageCopier:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = Path(source_folder)
        self.destination_folder = Path(destination_folder)

    def get_image_list(self):
        """Returns a list of image files in the source folder."""
        return [f.name for f in self.source_folder.iterdir() if f.is_file()]

    def exif_apple(self, image):
        """Returns the value of the EXIF tag 271 (Make) for the given image file."""
        try:
            img = Image.open(image)
            exif_data = img.getexif()
            return exif_data.get(271)
        except (AttributeError, IOError):
            pass

    def copy_apple_images(self):
        """Copies all images taken with an Apple device from the source folder to the destination folder."""
        # Check if source and destination folders exist
        if not self.source_folder.exists():
            logging.error(f"Source folder {self.source_folder} does not exist.")
            return
        if not self.destination_folder.exists():
            logging.error(f"Destination folder {self.destination_folder} does not exist.")
            return

        # Get list of image files in source folder
        image_list = self.get_image_list()

        # Copy Apple images to destination folder
        for image_filename in image_list:
            image_path = self.source_folder / image_filename
            if self.exif_apple(image_path) == 'Apple':
                logging.info(f"Copying {image_filename} to {self.destination_folder}")
                shutil.copy2(image_path, self.destination_folder)