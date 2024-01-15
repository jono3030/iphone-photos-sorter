from pathlib import Path
import shutil
import piexif

source_folder = Path("")
destination_folder = Path("")

image_list = [f for f in source_folder.iterdir() if f.is_file()]

for image in image_list:
    try:
        exif_data = piexif.load(image)
        if exif_data.get("0th", {}).get(271) == b'Apple':
            print(f"Copying {image.name} to {destination_folder}")
            shutil.copy2(image, destination_folder / image.name)
    except Exception as e:
        print(f"An error occurred while processing {image.name}: {e}")
