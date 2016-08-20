#!/usr/pkg/bin/tcsh

mkdir result
mkdir result/training
mkdir result/testing

if [ -e result/tp_fp.csv ]; then
	rm result/tp_fp.csv
fi

python3 feature_extract.py train/face/ training
python3 feature_extract.py train/non-face/ training
python3 feature_extract.py test/face/ testing
python3 feature_extract.py test/non-face/ testing
