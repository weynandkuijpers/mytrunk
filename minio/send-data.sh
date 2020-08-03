#!/bin/bash

WORKDIR="/root/opt/mytrunk/minio-test"
SSMALL="$WORKDIR/myharddisk-1MB.img"
SMALL="$WORKDIR/myharddisk-10MB.img"
MEDIUM="$WORKDIR/myharddisk-100MB.img"
LARGE="$WORKDIR/myharddisk-1GB.img"

./mc alias set gallen http://172.25.2.2:9000/

SSMALLS=10
SMALLS=10
MEDIUMS=100
LARGES=1000

BUCKET="gallen/001"

DSIZE=0

# for loop that executes a routine a number of times
for round in {1..1}
do

	for num in {1..5}
	do
		mc cp $LARGE $BUCKET/large.$num
		DSIZE=$(($DSIZE+LARGES))
		echo "LARGE $num done, trasnferred: $DSIZE"
		for numtoo in {1..5}
			do
			mc cp $MEDIUM $BUCKET/medium.$numtoo 
			DSIZE=$(($DSIZE+MEDIUMS))
			echo "MEDIUM $numtoo done, trasnferred: $DSIZE"
			for numtree in {1..5}
			do
				mc cp $SMALL $BUCKET/small.$numtree
				DSIZE=$(($DSIZE+SMALLS))
				echo "SMALL $numtree done, trasnferred: $DSIZE"
			done
		done

	done
	mc cp $LARGE $BUCKET/large.$num 
	DSIZE=$(($DSIZE+LARGES))
	echo "LARGE $num done, trasnferred: $DSIZE"
	echo "ROUND: $round done"

done
