while read line
do
   orig=$(echo "$line" | cut -d "," -f 1,2)
   ald=$(echo "$line" | cut -d "," -f 6)
   orig+=",'"
   orig+="$ald"
   orig+="'"
    echo "$orig" >> removedColums.txt
done < $1
