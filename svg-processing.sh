#!/bin/bash

# Define a function for the process command
process_svg() {
    svg_file="$1"
    # Extract the directory path without the filename
    dir_path=$(dirname "$svg_file")

    # Extract the base filename (without extension) from the SVG file
    base_filename=$(basename "$svg_file" .svg)

    # Create the output filename by appending -32x.webp to the base filename
    output_file_32="$dir_path/$base_filename-32x.webp"
    output_file_64="$dir_path/$base_filename-64x.webp"
    output_file_128="$dir_path/$base_filename-128x.webp"

    output_file_svg_min="$dir_path/$base_filename.min.svg"

    svgo -q --config "./svgo.config.js" "$svg_file" -o "$output_file_svg_min"

    # Run the convert command from imagemagick
    convert -background none -density 96 -quality 90 "$svg_file" "$output_file_32"
    convert -background none -density 192 -quality 90 "$svg_file" "$output_file_64"
    convert -background none -density 384 -quality 90 "$svg_file" "$output_file_128"

}

# Export the function so GNU Parallel can use it
export -f process_svg

# Find all instances of svg files (NOT minified ones, if doing re-processing for some reason) 
# in subdirectories and use GNU Parallel to process them in parallel
find assets/ -type f \( -name "color.svg" -o -name "flat.svg" \) | parallel -j3 --eta process_svg
