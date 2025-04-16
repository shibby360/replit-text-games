#!/bin/bash

if [ "$1" == "-d" ]; then
    echo "downloading"
    mkdir $2
    for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$2/files); do
        if ! [ "$(basename $files)" == "files" ]; then
            mkdir -p "$(dirname $file)"
            wget "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" -O $file &> /dev/null
            echo downloaded $file
        fi
    done
    cd ..
elif [ "$1" == "-u" ]; then
    for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/files); do
        curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" > temp.txt
        if cmp -s temp.txt $file; then
            :
        else
            echo "Updates needed for $2"
            echo "Making updates for $2"
            echo "deleting $2 directory"
            rm -r $2
            echo "removed, now reinstalling"
            ./manager.sh -d $2
            echo "fully updated"
        fi
    done
    rm temp.txt
elif [ "$1" == "-s" ]; then
    curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/manager.sh" > temp.txt
    if cmp -s temp.txt manager.sh; then
        :
    else
        mv temp.txt manager.sh
        echo "new manager.sh file"
    fi
else
    echo "-d <game name> to download"
    echo "-u <game name> to update"
    echo "-s to update manager file"
fi
