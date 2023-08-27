ServerListInput="Server1,Server2,Server4,Server3,Server5"
ServerList=ServerListInput.split(sep=",")   #You can also save in same variable. like (ServerList=ServerList.split(sep=","))
ExcludeListInput="Server2,Server5"
ExcludeList=ExcludeListInput.split(sep=",")

for Exclude in ExcludeList:
        ServerList.remove(Exclude)
print (ServerList)

'''
#!/bin/bash

ServerList="Server1,Server2,Server3,Server4,Server5"
Exclude="Server2,Server5"

for Ex in $(echo ${Exclude} | tr "," " ")
do
A=$(echo ${ServerList} | sed "s/${Ex}//g")
ServerList=$( echo ${A} | tr -s ',' )
done

echo ${ServerList} | sed "s/^,//g ; s/,$//g"
'''
