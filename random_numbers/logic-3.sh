##################################################################
## This script generates unique random numbers from range [1-10]
## Script use shuffle Linux builtin command
################################################################## 

#!/bin/bash

#using bash builtin command shuffle

#define range & count of numbers to print
numbers=($(shuf -i 1-10 -n 10))

#display numbers

echo "${numbers[@]}"

