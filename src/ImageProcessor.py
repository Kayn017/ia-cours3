import os
from PIL import Image
from datetime import datetime


class ImageProcessor:
    PROCESSED_FOLDER_PATH = "dataset"

    def __init__(self, path: str):
        self.path = path

    def _create_processed_folder(self) -> str:
        folder_path = os.path.join(
            self.PROCESSED_FOLDER_PATH, datetime.now().strftime("%Y%m%d%H%M%S")
        )

        if not os.path.exists(self.PROCESSED_FOLDER_PATH):
            raise FileNotFoundError(f"Folder {self.PROCESSED_FOLDER_PATH} not found")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    def _get_dimensions(self, size: int, image: Image.Image) -> tuple[int, int]:
        """
        Get the new dimensions for the image with the correct aspect ratio

        :param size: wanted size
        :param image: image that will be resized
        :return: tuple with the new dimensions
        """
        width, height = image.size

        if width > height:
            new_width = size
            new_height = int(size * height / width)
        elif width < height:
            new_width = int(size * width / height)
            new_height = size
        else:
            new_width = new_height = size

        return new_width, new_height

    def _add_padding(self, image: Image.Image) -> Image.Image:
        """
        Add padding to the image to make it square

        :param image: image that will be padded (The image must be resized before)
        :return: padded image
        """
        width, height = image.size

        if width == height:
            return image
        else:
            new_image = Image.new("RGB", (height, height), (114, 114, 114))
            new_image.paste(image, (0, 0))
            return new_image

    def _process_image(self, file: str, size: int, dest: str) -> None:
        """
        Resize and pad the image

        :param file: name of the image file
        :param size: wanted size
        :param dest: destination folder
        """
        file_path = os.path.join(self.path, file)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Image {file_path} not found")

        if not os.path.exists(dest):
            raise FileNotFoundError(f"Destination folder {dest} not found")

        print(f"Processing image {file}...")
        image = Image.open(file_path).convert("RGB")

        width, height = self._get_dimensions(size, image)

        image.resize((width, height))

        result = self._add_padding(image)

        result.save(os.path.join(dest, file))

        print(f"Image {file} processed")

    def process_folder(self, size: int) -> None:
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Folder {self.path} not found")

        folder = self._create_processed_folder()

        for file in os.listdir(self.path):
            if file.endswith((".jpg", ".png", ".gif")):
                self._process_image(file, size, folder)
