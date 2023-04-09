#!/bin/bash
#################################################################################
# Description	: Shell Script to take backup of network device config backup	#
# Author		: Kartheek Varma Kadumuru										#
# Version		: 1.0.0.0														#
#################################################################################

KDATE=$(date +%Y%m%d_%H%M%S)
FileInput=$1
FailedIPList=$( cat ${FileInput} )

NWDevUser=''
NWDevPass=''
NWDevPort='22'
NWDevIP=''

Srv1UserName=''
Srv1Pass=''
Srv1IP=''
Srv1DestPath=''
Srv1Port=''

Srv2UserName=''
Srv2Pass=''
Srv2IP=''
Srv2DestPath=''
Srv2Port=''

if [[ $# -neq 1 ]]
	then
	echo -e "$(basename) <InputFile>"
	exit 1
	else
	if [[ ! -f ${FileInput} ]]
		then
		echo -e "\tFailedDevice File(${FileInput}) not available in $(pwd) Path"
		exit 1
		else
		echo -e "\tFailedDevice File(${FileInput}) available in $(pwd) Path"
	fi
fi

function FunShowStartupConfig()
{
	ShowStartupConfig=""
	ShowStartupConfig=$(sshpass -p ${NWDevPass} ssh -p ${NWDevPort} -o "StrictHostKeyChecking=no" ${NWDevUser}@${NWDevIP} "show startup-config" ) &> /dev/null
	echo ${ShowStartupConfig} | sed "s/|/\r\n/g" > ${Srv1DestPath}/.txt
}

function FunShowRunningConfig()
{
	ShowRunningConfig=""
	ShowRunningConfig=$(sshpass -p ${NWDevPass} ssh -p ${NWDevPort} -o "StrictHostKeyChecking=no" ${NWDevUser}@${NWDevIP} "show running-config" ) &> /dev/null
	echo ${ShowRunningConfig} | sed "s/|/\r\n/g" > ${Srv1DestPath}/.txt
}

function FunShowIPInterfaceBrief()
{
	ShowIPInterfaceBrief=""
	ShowIPInterfaceBrief=$(sshpass -p ${NWDevPass} ssh -p ${NWDevPort} -o "StrictHostKeyChecking=no" ${NWDevUser}@${NWDevIP} "show IP interface brief" ) &> /dev/null
	echo ${ShowIPInterfaceBrief} | sed "s/|/\r\n/g" > ${Srv1DestPath}/.txt
}

function FunCreateDironSrv2()
{
	sshpass -p ${NWDevPass} ssh -p ${NWDevPort} -o "StrictHostKeyChecking=no" ${NWDevUser}@${NWDevIP} "mkdir -pv ${Srv2DestPath}"
	Srv2DestPathCheck=$( sshpass -p ${NWDevPass} ssh -p ${NWDevPort} -o "StrictHostKeyChecking=no" ${NWDevUser}@${NWDevIP} "IFCONDITION_HERE" )
	
	if [[ ${} == SUCCESS ]] ; then echo SUCCESS ; else echo FailedIPList ; fi
	
	sshpass -p ${Srv2Passwd} scp -P ${Srv2Port} -o "StrictHostKeyChecking=no" ${Srv1DestPath}/FILES_HERE.TXT ${Srv2UserName}@${Srv1IP} ${Srv2DestPath}/
	sshpass -p ${Srv2Passwd} ssh -p ${Srv2Port} -o "StrictHostKeyChecking=no" ${Srv2UserName}@${Srv1IP} "IFCONDITION_TOCHECK_COPIED_FILES"
}

