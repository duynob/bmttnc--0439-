import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0

    # Convert message to binary, 8 bits per character
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Add a termination sequence to the binary message
    binary_message += '1111111111111110'  # Dấu kết thúc thông điệp

    data_index = 0
    for row in range(height):
        for col in range(width):
            if data_index >= len(binary_message):
                break

            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3): # Iterate through R, G, B channels
                if data_index < len(binary_message):
                    # Modify the least significant bit of the color channel
                    # by replacing it with a bit from the binary message
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))
        
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'logohutech30nam.jpg'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()