mkdir $1
cd $1
for file in $(curl https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$1/files); do
    wget "https://raw.githubusercontent.com/shibby360/replit-text-games/refs/heads/main/$file"
done
cd ..