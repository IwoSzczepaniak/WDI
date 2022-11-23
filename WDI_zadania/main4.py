#!/bin/bash
if [ $# -gt 1 ]; then
	echo "za dużo argumentów"
	exit 1
fi
if [ ! -d $0 ]; then
    echo "to nie jest katalog, badz nie istnieje"
    exit 1
fi

if [ $# -eq 0 ]; then
    pliki=`ls -l | awk '{print $9}'`
    for plik in $pliki; do
        if [ -f $plik ]; then
                owner_name=`ls -l $plik | awk '{print $3}'`
                size=`stat -c %s $plik`
                if [ -x $plik ]; then
                    dostep="WYK"
                else
                    dostep="NIEWYK"
                fi

                echo "$plik $owner_name $size $dostep"
        fi
      done

else
    pliki=`ls -l $0 | awk '{print $9}'`
    for plik in $pliki; do
        if [ -f $plik ]; then
                owner_name=`ls -l $plik | awk '{print $3}'`
                size=`stat -c %s $plik`
                if [ -x $plik ]; then
                    dostep="WYK"
                else
                    dostep="NIEWYK"
                fi
                echo $plik "$owner_name $size $dostep"
        fi
    done
fi
exit 0