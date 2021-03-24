#!/bin/bash
for file in NENE*.txt;
do
sort -r $file|sed -n '1p;5p;$p'|paste - - - 
done
