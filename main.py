from src.ImageProcessor import ImageProcessor
import argparse


def main():
    parser = argparse.ArgumentParser(description="Image processing pipeline")

    parser.add_argument(
        "--folder_path",
        type=str,
        help="Path to the folder containing all images to process",
    )
    parser.add_argument(
        "--resolution", type=int, help="Resolution of the processed image"
    )

    args = parser.parse_args()

    folder_path = args.folder_path
    resolution = args.resolution

    processor = ImageProcessor(folder_path)
    processor.process_folder(resolution)


if __name__ == "__main__":
    main()
