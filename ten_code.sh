#!/bin/bash
number_of_files=$(ls -1q| wc -l)
oldest_file=$(ls -lt -1|tail -1|cut -c34-100)
newest_file=$(ls -lt -1|head -2|tail -1|cut -c34-100)
smallest_file_size=$(ls -lS -1|tail -1|cut -c30-33)
smallest_file=$(ls -lS -1|tail -1|cut -c47-100)
largest_file_size=$(ls -lS -1|head -2|tail -1|cut -c30-33)
largest_file=$(ls -lS -1|head -2|tail -1|cut -c47-100)
echo $number_of_files, $oldest_file, $newest_file, smallest file = $smallest_file,smallest file size = $smallest_file_size, largest file = $largest_file largest file size = $largest_file_size

