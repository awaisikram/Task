############################################################
## This script generates random numbers from range [1-10]
## Scripts executes until all unique numbers are printed
###########################################################
#!/bin/bash

#Range of numbers 1-10
x=1
y=10
#while loop until array has 10 items
while [ "$x" -le "$y" ];
do
    #Generating RANDOM number
    a=$(($RANDOM %10 +1))
    #condition to check unique number in array
    if [[ "${num[@]}" =~ "$a" ]]; then
        #only for debug
        echo "already in array" 
        echo $a
        echo "${num[@]}"
        #1 sec pause to see results
        sleep 1

    else
        #add number to array
        num[$x]=$a
        # increasing value of x by 1
        let x=x+1
    fi
done

#Display the array
echo "${num[@]}"



