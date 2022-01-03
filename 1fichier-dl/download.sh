#!/bin/bash
while IFS=" " read -r i j
do
       python3 cli_aria2.py $i $j
done < $1
