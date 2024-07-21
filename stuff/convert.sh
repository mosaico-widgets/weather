#!/bin/bash

# Directory containing the downloaded images
input_dir="weather_images"
# Directory to save the converted images
output_dir="weather_images_ppm"

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through each image in the input directory
for img in "$input_dir"/*.png; do
  # Extract the filename without extension
  filename=$(basename "$img" .png)
  # Convert and resize the image to PPM format with black background
  convert "$img" -resize 32x32 -background black -gravity center -extent 32x32 "$output_dir/$filename.ppm"
done

echo "Conversion complete. Check the '$output_dir' directory for the PPM files."

