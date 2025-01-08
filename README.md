# Steganography Tool

This tool is a graphical user interface (GUI) application built using Python and CustomTkinter for encoding and decoding text within images. It allows users to securely hide messages inside images and retrieve them whenever needed.

---

## Features

### 1. **Image Preview**
   - Allows users to preview the selected image before encoding or decoding.
   - Automatically resizes and centers the image within a defined preview area while maintaining its aspect ratio.

### 2. **Text Encoding**
   - Users can enter text to hide within the image.
   - Encodes text in the image by manipulating the least significant bit (LSB) of the image pixels.

### 3. **Text Decoding**
   - Allows users to retrieve hidden text from encoded images.
   - Prompts users to select the image for decoding.

### 4. **Save Encoded Image**
   - Saves the encoded image with a modified filename in the same directory as the original image.

### 5. **User-Friendly Interface**
   - Built with CustomTkinter for a modern and responsive design.
   - Buttons, labels, and text fields are well-organized for ease of use.

---

## Installation

### Prerequisites
- Python 3.8 or later
- `pip` package manager

### Required Libraries
Install the required Python libraries using the following command:

```bash
pip install customtkinter pillow
```

---

## Usage

### Running the Application
Run the `Steganography.py` file in your Python environment:

```bash
python Steganography.py
```

### Steps
1. **Select an Image**:
   - Click the "Select Image" button and choose an image file (PNG, JPG, or JPEG).
   - The image will be displayed in the preview area.

2. **Encode Text**:
   - Enter the text you want to hide in the provided text field.
   - Click the "Encode Text" button to hide the text in the selected image.

3. **Save Encoded Image**:
   - Click the "Save Encoded Image" button to save the modified image.
   - The encoded image will be saved in the same directory as the original image with a `_encoded` suffix.

4. **Decode Text**:
   - Click the "Decode Text" button to select an image containing hidden text.
   - The hidden text will be retrieved and displayed in a pop-up message.


---

## Notes
- Ensure the images used for encoding and decoding are in PNG, JPG, or JPEG format.
- The text encoding process appends a unique delimiter (`1111111111111110`) to mark the end of the hidden message.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

---

## Author

- GitHub: [@4LPH7](https://github.com/4LPH7)

Feel free to contribute or suggest improvements!

---
### Show your support

Give a ⭐ if you like this website!

<a href="https://buymeacoffee.com/arulartadg" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-violet.png" alt="Buy Me A Coffee" height= "60px" width= "217px" ></a>


