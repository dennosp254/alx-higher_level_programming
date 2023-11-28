#!/bin/bash

# Check if a file path is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Get the file path from the command line argument
file_path=$1

# Check if the file exists
if [ ! -e "$file_path" ]; then
    echo "Error: File not found: $file_path"
    exit 1
fi

# Make the file executable for the owner (user)
chmod u+x "$file_path"

echo "File $file_path is now executable for the owner."
