dist=0
for i in {2..50}
	do
		echo "$i clusters init"
		python kMeans.py doc2vectrain.csv $i $dist
		echo "$i clusters eval"
		python internalValidation.py result.txt "$i"clustersWith"$dist"model doc2vectrain.csv 
	done
