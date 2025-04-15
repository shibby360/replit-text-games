files=$(ls $1)
for i in $files; do
    if [ -d "$1/$i" ]; then
        ./list.sh "$1/$i"
    else
        echo $1/$i
    fi
done