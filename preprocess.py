from PIL import Image
import os

def preprocess(input_dir, input_file, output_dir, counter, quality=95, export=True, size=(256, 256)):
    """
    Preprocess a single image: resize and save with specified quality.
    Args:
        input_dir (str): Directory of the input image.
        input_file (str): Name of the input image file.
        output_dir (str): Directory to save the processed image.
        counter (int): Counter for naming the output file.
        quality (int, optional): Quality for saving JPEG images. Defaults to 95.
        export (bool, optional): Whether to save the processed image. Defaults to True.
        size ((int, int), optional): Size to resize the image to. Defaults to (256, 256).
    Returns:
        PIL.Image or None: The processed image if export is False, otherwise None.
    """
    if input_file.lower().endswith(('.jpg', '.jpeg')):
        img_path = os.path.join(input_dir, input_file)
        try:
            img = Image.open(img_path)
            img_resized = img.resize(size)

            if not (export):
                return img_resized

            output_input_file = f'frame_{counter:06d}.jpg'
            output_path = os.path.join(output_dir, output_input_file)
            img_resized.save(output_path, "JPEG", quality=quality)
        except Exception as e:
            print(f"Error processing {input_file}: {e}")