#!/bin/sh
if [ -z "$CXX" ];
then
    CXX=g++
fi

TESTS=0
SUCCESS=0
for cppfile in *.cpp;
do
    TESTS=$((TESTS + 1))
    $CXX -std=c++14 $cppfile -o $cppfile.out 
    COMPILATION=$?
    if [ $COMPILATION -eq 0 ];
    then
        ./$cppfile.out
        TEST_SUCCESS=$?
        if [ $TEST_SUCCESS -eq 0 ];
        then
            SUCCESS=$((SUCCESS + 1))
        else
            echo "Test $cppfile failed!"
        fi
    else
        echo "Error while compiling $cppfile!"
    fi
done

rm *.cpp *.cpp.out

echo
echo "$SUCCESS / $TESTS tests were successful."
if [ $SUCCESS -eq $TESTS ];
then
    exit 0
else
    exit 1
fi
