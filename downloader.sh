declare -A files
files["sk-uv"]="bases.py enemys.py heros.py idgen.py main.py weapons.py"
files["u-v"]="main.py"
files["water-gun-war"]="main.py"
files["text-village-game"]="buildings.py main.py troops.py"
files["cpp-card-game"]="card-game.cpp"
files["type-teams"]="enemies/circuitizer.py enemies/massdark.py teams/hot/__init__.py teams/secreteam/__init__.py teams/storm/__init__.py teams/transform/__init__.py teams/__init__.py main.py"
files["me-and-others"]="main.py"
mkdir $1
cd $1
for file in ${files[$1]}; do
    wget "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/$file"
done
cd ..