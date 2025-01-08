from PIL import Image

def encode_text(image_path, text, output_path):
    # Open the image
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size
    pixels = encoded_image.load()

    # Convert text to binary
    binary_text = ''.join([format(ord(char), '08b') for char in text])
    
    # Append delimiter to indicate end of text
    binary_text += '1111111111111110'

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_text):
                pixel = list(pixels[x, y])
                for n in range(3):  # Iterate over RGB
                    if data_index < len(binary_text):
                        pixel[n] = pixel[n] & ~1 | int(binary_text[data_index])
                        data_index += 1
                pixels[x, y] = tuple(pixel)
            else:
                break

    # Save the encoded image
    encoded_image.save(output_path)
    print(f"Text encoded and saved to {output_path}")

# Example usage
encode_text('input_image.png', 'Hello, World!', 'encoded_image.png')