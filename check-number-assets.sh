#!/bin/bash

search_dir="assets/"
found_issue=0

find "$search_dir" -mindepth 1 -type d | while read -r dir; do
  file_count=$(find "$dir" -maxdepth 1 -type f | wc -l)
  if [ "$file_count" -ne 10 ]; then
    echo "Folder $dir does not contain 10 files. It has $file_count files."
    found_issue=1
  fi
done