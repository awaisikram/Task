#!/bin/bash

#define mininum and maximum range
min=1
max=40

# starting loop for rang[1-10]
while [ "$min" -le "$max" ];
do
    #storing RANDOM number in an array
    num[$min]=$(($RANDOM %10 +1))
    #display array numbers
    echo "${num[@]}"
#    sleep 1
    #increasing value of min by 1
    let min=min+1
done

# sorting & Remove duplicate from array num[] and store unique numbers in array final[]
final=($(printf "%s\n" ${num[@]} | sort | uniq ))

#Display unique array numbers
echo "Unique number array =" "["  "${final[@]}"  "]"

#################################################################


