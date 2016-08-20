#!/bin/bash

sed 's/ \+/ /g' $1/mfeat-fac | sed 's/ /,/g' > result/mfeat_fac
sed 's/ \+/ /g' $1/mfeat-kar| sed 's/ /,/g' > result/mfeat_kar
sed 's/ \+/ /g' $1/mfeat-fou | sed 's/ /,/g' > result/mfeat_fou
sed 's/ \+/ /g' $1/mfeat-zer | sed 's/ /,/g' > result/mfeat_zer
sed 's/ \+/ /g' $1/mfeat-mor | sed 's/ /,/g' > result/mfeat_mor
sed 's/ \+/ /g' $1/mfeat-pix | sed 's/ /,/g' > result/mfeat_pix


paste result/mfeat_fac result/mfeat_kar result/mfeat_fou result/mfeat_zer result/mfeat_mor result/mfeat_pix > result/mfeat_f
sed 's/\t//g' result/mfeat_f | sed 's/^,//g' | sed 's/$/,/g' > result/mfeat_5

paste result/mfeat_5 classes.txt > result/mfeat_final
sed -i 's/\t//g' result/mfeat_final

foreach i (0 200 400 600 800 1000 1200 1400 1600 1800)
	awk "NR==1 + ${i}, NR==100 + ${i} {print $2}" result/mfeat_final >> result/mfeat_training.arff
end
foreach i (100 300 500 700 900 1100 1300 1500 1700 1900)
	awk "NR==1 + ${i}, NR==100 + ${i} {print $2}" result/mfeat_final >> result/mfeat_testing.arff
end

cat variable_define.txt result/mfeat_testing.arff > result/mfeat-test.arff
cat variable_define.txt result/mfeat_training.arff > result/mfeat-train.arff

