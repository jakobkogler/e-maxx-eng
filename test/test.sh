#!/bin/sh
./extract_test.py
for cppfile in *.cpp;
do
    g++ -std=c++14 $cppfile -o $cppfile.out && ./$cppfile.out
    rm $cppfile $cppfile.out
done
