from PIL import Image
import os

# --- CHANGE THIS LINE TO YOUR PRODUCT FOLDER ---
folder_path = "mrr-image"  # <-- Change this if your product folder has a different name!

# Loop through every file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".webp", ".jpg", ".jpeg", ".png")):
        file_path = os.path.join(folder_path, filename)
        
        # Open the image
        with Image.open(file_path) as img:
            # Double the size
            new_size = (img.width * 2, img.height * 2)
            
            # Resize with high-quality filtering
            upscaled_img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save it back to the exact same file (overwriting the old one)
            upscaled_img.save(file_path, quality=95)
            print(f"✅ Upgraded: {filename}")

print("\n🎉 All product images upgraded in the same folder!")