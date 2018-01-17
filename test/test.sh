#!/bin/sh
for cppfile in *.cpp;
do
    $CXX -std=c++14 $cppfile -o $cppfile.out && ./$cppfile.out
    rm $cppfile $cppfile.out
done
