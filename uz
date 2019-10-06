#!/bin/bash

args=`getopt t:e:h $*`
if [ $? != 0 ]
then
	echo 'Usage: uz [-t|--target <targetPath>] [-e|--encoding <encoding>] filename[.zip]'
    exit 2
fi
set -- $args
target="$PWD"
encoding="big5"
for i
do
	case "$i"
    in
		-t)
			target="$2";
			shift;
			shift;;
		-e)
			encoding="$2"; 
			shift;
			shift;;
		-h)
			echo "Usage: uz [-t|--target <targetPath>] [-e|--encoding <encoding>] filename[.zip]"
			exit 2
			;;
		--)
			shift; break;;
	esac
done
for i in $@; do :; done

python unzip.py $target $encoding "/"$i

echo Done!
