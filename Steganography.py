import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Initialize CustomTkinter theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class SteganographyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure main window
        self.title("Image Steganography Tool")
        self.geometry("800x450")
        self.minsize(800, 500)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # Variables
        self.image_path = None
        self.preview_image = None

        # Left-side panel
        self.left_panel = ctk.CTkFrame(self, width=300, corner_radius=10)
        self.left_panel.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.left_panel.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=0)

        # Buttons and Entry Fields
        self.title_label = ctk.CTkLabel(self.left_panel, text="Steganography Tool", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.select_image_button = ctk.CTkButton(self.left_panel, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=1, column=0, padx=20, pady=10)

        self.text_entry = ctk.CTkEntry(self.left_panel, placeholder_text="Enter text to encode")
        self.text_entry.grid(row=2, column=0, padx=20, pady=10)

        self.encode_button = ctk.CTkButton(self.left_panel, text="Encode Text", command=self.encode_text)
        self.encode_button.grid(row=3, column=0, padx=20, pady=10)

        self.decode_button = ctk.CTkButton(self.left_panel, text="Decode Text", command=self.decode_text)
        self.decode_button.grid(row=4, column=0, padx=20, pady=10)

        self.save_button = ctk.CTkButton(self.left_panel, text="Save Encoded Image", command=self.save_encoded_image)
        self.save_button.grid(row=5, column=0, padx=20, pady=10)

        # Center preview area
        self.preview_frame = ctk.CTkFrame(self, corner_radius=10)
        self.preview_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.preview_frame.grid_rowconfigure(0, weight=0)  # For the label
        self.preview_frame.grid_rowconfigure(1, weight=1)  # For the canvas
        self.preview_frame.grid_columnconfigure(0, weight=1)

        self.preview_label = ctk.CTkLabel(self.preview_frame, text="Image Preview", font=("Arial", 18))
        self.preview_label.grid(row=0, column=0, pady=(20, 10))

        self.image_canvas = ctk.CTkCanvas(self.preview_frame, bg="gray", width=600, height=400, highlightthickness=0)
        self.image_canvas.grid(row=1, column=0, padx=20, pady=20, sticky="nswe")

    def select_image(self):
        filetypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
        self.image_path = filedialog.askopenfilename(title="Select an Image", filetypes=filetypes)

        if self.image_path:
            # Open the selected image
            original_image = Image.open(self.image_path)
            img_width, img_height = original_image.size

            # Define the preview canvas size
            canvas_width, canvas_height = 1000, 800

            # Adjust the image size to fit within the canvas while maintaining aspect ratio
            if img_width > canvas_width or img_height > canvas_height:
                scale = min(canvas_width / img_width, canvas_height / img_height)
                new_width = int(img_width * scale)
                new_height = int(img_height * scale)
            else:
                # If the image is smaller than the canvas, keep its original size
                new_width, new_height = img_width, img_height

            resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
            self.preview_image = ImageTk.PhotoImage(resized_image)

            # Clear canvas and draw the centered image
            self.image_canvas.delete("all")
            x_offset = (canvas_width - new_width) // 2
            y_offset = (canvas_height - new_height) // 2
            self.image_canvas.create_image(x_offset, y_offset, image=self.preview_image, anchor="nw")
            self.image_canvas.update()

    def encode_text(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return

        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "No text provided.")
            return

        try:
            image = Image.open(self.image_path)
            encoded_image = image.copy()
            width, height = image.size
            pixels = encoded_image.load()

            binary_text = ''.join([format(ord(char), '08b') for char in text])
            binary_text += '1111111111111110'

            data_index = 0
            for y in range(height):
                for x in range(width):
                    if data_index < len(binary_text):
                        pixel = list(pixels[x, y])
                        for n in range(3):  # RGB
                            if data_index < len(binary_text):
                                pixel[n] = pixel[n] & ~1 | int(binary_text[data_index])
                                data_index += 1
                        pixels[x, y] = tuple(pixel)

            self.encoded_image = encoded_image
            messagebox.showinfo("Success", "Text successfully encoded!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decode_text(self):
        # Prompt the user to select an image for decoding
        filetypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
        decode_image_path = filedialog.askopenfilename(title="Select an Image for Decoding", filetypes=filetypes)

        if not decode_image_path:
            messagebox.showerror("Error", "No image selected for decoding.")
            return

        try:
            image = Image.open(decode_image_path)
            pixels = image.load()
            width, height = image.size

            binary_text = ""
            for y in range(height):
                for x in range(width):
                    pixel = pixels[x, y]
                    for n in range(3):  # RGB
                        binary_text += str(pixel[n] & 1)

                        if binary_text.endswith('1111111111111110'):
                            binary_text = binary_text[:-16]
                            text = "".join(
                                chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8)
                            )
                            messagebox.showinfo("Decoded Text", text)
                            return

            messagebox.showwarning("No Text Found", "No hidden text detected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_encoded_image(self):
        if not hasattr(self, 'encoded_image'):
            messagebox.showerror("Error", "No encoded image to save.")
            return

        input_dir, input_name = os.path.split(self.image_path)
        output_name = f"{os.path.splitext(input_name)[0]}_encoded.png"
        output_path = os.path.join(input_dir, output_name)

        try:
            self.encoded_image.save(output_path)
            messagebox.showinfo("Success", f"Encoded image saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")


# Run the application
if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()
