import os
import sys

# Add packages directory to sys.path
package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages')
sys.path.insert(0, package_dir)

# Import bundled packages
from PIL import Image, ImageEnhance
import termcolor

where_termcolor = termcolor.__file__
where_PIL_Image = Image.__file__
where_PIL_ImageEnhance = ImageEnhance.__file__
print(f'{termcolor.colored("[Info]", "black", "on_yellow")}: Using package from {termcolor.colored(where_termcolor, "yellow")}')
print(f'{termcolor.colored("[Info]", "black", "on_yellow")}: Using package from {termcolor.colored(where_PIL_Image, "yellow")}')
print(f'{termcolor.colored("[Info]", "black", "on_yellow")}: Using package from {termcolor.colored(where_PIL_ImageEnhance, "yellow")}')

# Set input and output folders
input_folder = r'C:\Users\Daniel\AppData\Roaming\PrismLauncher\instances\Vibracraft\.minecraft\resourcepacks\VibraCraft\assets\minecraft\textures\trims\em'
output_folder = r'C:\Users\Daniel\AppData\Roaming\PrismLauncher\instances\Vibracraft\.minecraft\resourcepacks\VibraCraft\assets\minecraft\textures\trims'

# Set saturation factor
saturation_factor = 1.75

# Process subfolders flag
sub_folders = True

def process_folder(input_folder, output_folder, subdir=''):
    for filename in os.listdir(os.path.join(input_folder, subdir)):
        # Check if the file is an image
        if filename.endswith('.png'):
            # Open image and convert to RGBA mode if needed
            with Image.open(os.path.join(input_folder, subdir, filename)) as image:
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')
                # Apply saturation enhancement
                color = ImageEnhance.Color(image)
                image = color.enhance(saturation_factor)
                # Save the new image to the output folder
                output_path = os.path.join(output_folder, subdir, filename)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                image.save(output_path, 'PNG')
                print(f'{termcolor.colored("[Main]", "black", "on_green")}: Processed {termcolor.colored(os.path.join(subdir, filename), "green")}')


    if sub_folders:
        # Recursively process subfolders
        for subfolder in os.listdir(os.path.join(input_folder, subdir)):
            if os.path.isdir(os.path.join(input_folder, subdir, subfolder)) and subfolder != 'defaults':
                process_folder(input_folder, output_folder, subdir=os.path.join(subdir, subfolder))



# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Check if input folder is empty
if not os.listdir(input_folder):
    print(f'{termcolor.colored("[WARN]", "black", "on_red")}: {termcolor.colored("Input folder", "red")} {termcolor.colored(input_folder, "black", "on_yellow")} {termcolor.colored("is empty.", "red")}')
else:
    # Process the input folder
    process_folder(input_folder, output_folder)
