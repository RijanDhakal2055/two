#!/bin/bash
for file in NENE*.txt;
do 
Number_of_lines=$(wc -l $file| cut -d ' ' -f1)
largest=$(sort $file -r| sed -n '$p')
smallest=$(sort $file -r| sed -n '1p')
fifth=$(sort $file -n| sed -n '5p')
echo $file $Number_of_lines, $largest , $smallest, $fifth
done
