from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
       image_array = np.array(image)
    
    # Encrypt the image by adding the key to each pixel
    encrypted_array = (image_array + key) % 256
    
    # Create an encrypted image from the array
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    image_array = np.array(image)
    
    # Decrypt the image by subtracting the key from each pixel
    decrypted_array = (image_array - key) % 256
    
    # Create a decrypted image from the array
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Example usage
# encrypt_image('input.png', 'encrypted_image.png', key=50)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=50)
