for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/files); do
        curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file" > temp.txt
        if cmp -s temp.txt $file; then
                :
        else
                echo "Updates needed for $1"
                echo "Making updates for $1"
                echo "deleting $1 directory"
                rm -r $1
                echo "removed, now reinstalling"
                ./downloader.sh $1
                echo "fully updated"
        fi
done
rm temp.txt
