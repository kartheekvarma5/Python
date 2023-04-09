#!/bin/bash

File=$1

mv ${File} Capture.png

python PythonOCR.py &> ${File}.txt

mv Capture.png ${File}

cat ${File}.txt | grep '\S' > temp.txt

mv temp.txt ${File}.txt

cat ${File}.txt