#!/bin/bash
TWOSUM() {
echo $[$1+$2]
}

for I in {1..10};
do
	let j=$[$I+1]
	echo $I plus $j is `TWOSUM $I $j` 	

done
