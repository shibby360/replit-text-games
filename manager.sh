#!/bin/bash

function usage() {
    echo "-d <game name> to download"
    echo "-u <game name> to update"
    echo "-s to update manager file"
    echo "-a to view all games"
}
allgames=$(curl -s -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/allgames")
function isGame() {
    echo "${allgames[@]}" | grep -F -q $1
}
while getopts ":d:u:sa" opt; do
    case "${opt}" in
        d)
            if ! isGame ${OPTARG}; then
                usage
                continue
            fi
            echo "downloading"
            mkdir ${OPTARG}
            for file in $(curl -s -H "Cache-Control: no-cache" https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/${OPTARG}/files); do
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
            if ! [ -d ${OPTARG} ]; then
                usage
                continue
            fi
            for file in $(curl -s -H "Cache-Control: no-cache" https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/${OPTARG}/files); do
                curl -s -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" > temp.txt
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
            curl -s -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/manager.sh" > temp.txt
            if cmp -s temp.txt manager.sh; then
                rm temp.txt
            else
                mv temp.txt manager.sh
                chmod 777 manager.sh
                echo "new manager.sh file"
            fi
            ;;
        a)
            echo "${allgames[@]}"
            ;;
        :)
            usage
            ;;
        ?)
            usage
            ;;
    esac
done

if ! [[ "$1" == -* ]]; then
    usage
fi
shift $((OPTIND-1))
