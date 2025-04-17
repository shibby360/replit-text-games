#!/bin/bash

while getopts ":d:u:sa" opt; do
    case "${opt}" in
        d)
            echo "downloading"
            mkdir ${OPTARG}
            for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/${OPTARG}/files); do
                if ! [ "$(basename $file)" == "files" ]; then
                    mkdir -p "$(dirname $file)"
                    wget "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" -O $file &> /dev/null
                    chmod 777 $file
                    echo downloaded $file
                fi
            done
            cd ..
            ;;
        u)
            for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/${OPTARG}/files); do
                curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" > temp.txt
                if cmp -s temp.txt $file; then
                    :
                else
                    echo "Updates needed for ${OPTARG}"
                    echo "Making updates for ${OPTARG}"
                    echo "deleting ${OPTARG} directory"
                    rm -r ${OPTARG}
                    echo "removed, now reinstalling"
                    ./manager.sh -d ${OPTARG}
                    echo "fully updated"
                fi
            done
            rm temp.txt
            ;;
        s)
            curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/manager.sh" > temp.txt
            if cmp -s temp.txt manager.sh; then
                :
            else
                mv temp.txt manager.sh
                chmod 777 manager.sh
                echo "new manager.sh file"
            fi
            ;;
        a)
            echo $(curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/allgames")
            ;;
        *)
            echo "-d <game name> to download"
            echo "-u <game name> to update"
            echo "-s to update manager file"
            echo "-a to view all games"
            ;;
    esac
done