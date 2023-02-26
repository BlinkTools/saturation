# BlinkTools: Saturation Changer

## Overview
This tool takes all `.png`/`.jpg` files from an `input_folder` and changes their saturation (by a `saturation_factor`) using Pillow (PIL) and puts the modified files into an `output_folder`.

## Usage
Open the `saturation.py` file in your favorite editor and change the path to the `input_folder` and `output_folder` (the script will warn you if the input folder is empty) and also change the `saturation_factor` (this is comparable with how the GIMP saturation works)

To actually run the script you do not have to have `Pillow (PIL)` or `termcolor` installed because they are included with the script in the `packages` folder.

## Planned Features
- Reduce Saturation