# This README will show you how to run the programs:

'% ' means the start of the command-line in Unix system.

#### Q1 folder:

* Edge detection, Noise cancellation, Image enhancement:
    - % python3 image-preprocessing.py
    - Follow the instruction shows by the program.
    - The results are saved to same folder as the input images.

#### Q2 folder:

* Image data mining:
    - % python3 threshold.py
    - The result is saved to the same folder as the input image.
    
* Face Detection:
    - % ./run.sh
    - % ./combine.sh
    - Find the training set from Q2/result/training/training.arff
    Find the testing set from Q2/result/testing/testing.arff
    - Import the training set and testing set to WEKA, choose Naive bayes as classifier, then observe the result.
    
#### Q3 folder:

* Classification of Hand-Written Digits:
    - % ./run.sh
    - Find the results from Q3/result/*
    - Import the results to WEKA, choose J48 as classifier, then observe the result.