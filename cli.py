import argparse
from iphone_photos_sorter import AppleImageCopier

class AppleImageCopierCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Copy Apple images from source to destination folder.')
        self.parser.add_argument('source_folder', help='Path to source folder')
        self.parser.add_argument('destination_folder', help='Path to destination folder')

    def run(self):
        args = self.parser.parse_args()
        copier = AppleImageCopier(args.source_folder, args.destination_folder)
        copier.copy_apple_images()

def main():
    cli = AppleImageCopierCLI()
    cli.run()

if __name__ == '__main__':
    main()