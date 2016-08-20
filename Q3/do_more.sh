#!/usr/pkg/bin/tcsh

sed 's/ \+/ /g' $1/mfeat-mor | sed 's/ /,/g' > result/mfeat_mor
sed 's/$/,/g' result/mfeat_mor > result/mfeat_mor_
paste result/mfeat_mor_ classes.txt > result/mfeat_mor_final
sed -i 's/^,//g' result/mfeat_mor_final
sed -i 's/\t//g' result/mfeat_mor_final


foreach i (0 200 400 600 800 1000 1200 1400 1600 1800)
	awk "NR==1 + ${i}, NR==100 + ${i} {print $2}" result/mfeat_mor_final >> result/mfeat_mor_train_fin.arff
end
foreach i (100 300 500 700 900 1100 1300 1500 1700 1900)
	awk "NR==1 + ${i}, NR==100 + ${i} {print $2}" result/mfeat_mor_final >> result/mfeat_mor_test_fin.arff
end

cat variable_mor.txt result/mfeat_mor_test_fin.arff > result/mfeat-mor-test.arff
cat variable_mor.txt result/mfeat_mor_train_fin.arff > result/mfeat-mor-train.arff
