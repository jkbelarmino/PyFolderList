from PIL import Image
import os

# Define source-target folder pairs
folders = [
    (r"TARGET FOLDER PATH", r"SOURCE FOLDER PATH"),
]

# Set target width
new_width = 300

# Process each folder
for source_folder, target_folder in folders:
    os.makedirs(target_folder, exist_ok=True)  # Create target folder if missing
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):  # Include GIFs in filtering
            img_path = os.path.join(source_folder, filename)
            img = Image.open(img_path)

            # Convert P-mode (palette) images to RGBA first to handle transparency
            if img.mode == "P":
                img = img.convert("RGBA")

            # Convert RGBA to RGB (JPEG does not support transparency)
            if img.mode == "RGBA":
                img = img.convert("RGB")

            # Calculate new height while maintaining aspect ratio
            aspect_ratio = img.height / img.width
            new_height = int(new_width * aspect_ratio)

            # Resize with high-quality LANCZOS resampling
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Save as JPEG format
            save_path = os.path.join(target_folder, os.path.splitext(filename)[0] + ".jpg")
            img.save(save_path, "JPEG")
            print(f"Resized & converted: {filename} to {new_width}x{new_height}")

print("Finished resizing all images.")
