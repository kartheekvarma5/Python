#!/bin/bash

InFile=$1
OutFile=Inventory_Out.txt
rm Inventory_Out.txt

List=($(cat ${InFile} | sed 's/#/\n/g ; s/: /:/g ; s/ :/:/g' |  awk -F ':' '{print $3}' | sort -u ))

for Fin in ${List[@]}
do
	Cnt=$(cat ${InFile} | sed 's/#/\n/g ; s/: /:/g ; s/ :/:/g' | grep ${Fin} | awk -F ':' '{print $3}' | wc -l )
	for Tot in $(cat ${InFile} | sed 's/#/\n/g ; s/: /:/g ; s/ :/:/g' | grep ${Fin} | awk -F ':' '{print $4}')
	do
		FinTot=$( expr ${FinTot} + ${Tot} )
	done
	echo ${Fin}:${Cnt}:${FinTot}
	FinTot=0
done | tee -a ${OutFile}