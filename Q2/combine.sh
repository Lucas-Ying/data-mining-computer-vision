#!/bin/bash

cat training_arff_header.csv result/training/face_dataset.csv result/training/non-face_dataset.csv > result/training/training.arff
cat testing_arff_header.csv result/testing/face_dataset.csv result/testing/non-face_dataset.csv > result/testing/testing.arff