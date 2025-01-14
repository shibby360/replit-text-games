declare -A files
files["sk-uv"]="bases.py enemys.py heros.py idgen.py main.py weapons.py"
files["u-v"]="main.py"
files["water-gun-war"]="main.py"
files["text-village-game"]="buildings.py main.py troops.py"
files["cpp-card-game"]="card-game.cpp"
mkdir $1
cd $1
for file in ${files[$1]}; do
    wget "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/$file"
done
cd ..