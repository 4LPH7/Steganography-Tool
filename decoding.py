from PIL import Image


def decode_text(image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    binary_text = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            for n in range(3):  # Iterate over RGB
                binary_text += str(pixel[n] & 1)

                # Check if the last 16 bits form the delimiter
                if binary_text.endswith('1111111111111110'):
                    binary_text = binary_text[:-16]  # Remove the delimiter
                    text = "".join(
                        chr(int(binary_text[i:i + 8], 2))
                        for i in range(0, len(binary_text), 8)
                    )
                    return text

    return ""  # Return an empty string if no text is found


# Example usage
decoded_text = decode_text('encoded_image.png')
print(f"Decoded text: {decoded_text}")
