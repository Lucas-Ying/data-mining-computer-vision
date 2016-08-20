#!/bin/bash

mkdir result

/usr/pkg/bin/tcsh ./do.sh ../project1-images/3.1/mfeat-digits/
/usr/pkg/bin/tcsh ./do_more.sh ../project1-images/3.1/mfeat-digits/
/usr/pkg/bin/tcsh ./clean.sh

