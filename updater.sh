declare -A files
files["sk-uv"]="bases.py enemys.py heros.py idgen.py main.py weapons.py"
files["u-v"]="main.py"
files["water-gun-war"]="main.py"
for file in ${files[$1]}; do
        curl "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/$file" > temp.txt
        if cmp -s temp.txt $1/$file; then
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
