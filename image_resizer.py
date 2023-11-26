from PIL import Image

# Get user input for image path
image_path = input("Enter the path of the image file: ")

# Get user input for new dimensions
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))

# Open and resize the image
try:
    original_image = Image.open(image_path)
    resized_image = original_image.resize((new_width, new_height))
    resized_image.save("resized_image.jpg")  # Change the file name and extension if needed
    print("Image resized successfully.")
except Exception as e:
    print(f"Error: {e}")
