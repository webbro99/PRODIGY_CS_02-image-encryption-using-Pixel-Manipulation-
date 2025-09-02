from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            encrypted_pixel = ((r + key) % 256, (g - key) % 256, (b + key) % 256)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            decrypted_pixel = ((r - key) % 256, (g + key) % 256, (b - key) % 256)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

 # image path
input_image = r"C:\Users\dhruv\Desktop\cs_project\dp.jpg"
encrypted_image = r"C:\Users\dhruv\Desktop\cs_project\encrypted_image.png"
decrypted_image = r"C:\Users\dhruv\Desktop\cs_project\decrypted_image.png"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=88)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=88)