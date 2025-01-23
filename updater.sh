declare -A files
files["sk-uv"]="bases.py enemys.py heros.py idgen.py main.py weapons.py"
files["u-v"]="main.py"
files["water-gun-war"]="main.py"
files["text-village-game"]="buildings.py main.py troops.py"
files["cpp-card-game"]="card-game.cpp"
files["type-teams"]="enemies/circuitizer.py enemies/massdark.py teams/hot/__init__.py teams/secreteam/__init__.py teams/storm/__init__.py teams/transform/__init__.py teams/__init__.py main.py"
files["me-and-others"]="main.py"
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
