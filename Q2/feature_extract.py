import sys
import os
import numpy
import csv
import threshold
from PIL import Image


def feature_percentage(row_start, row_end, col_start, col_end, img):
    '''
        The feature is a rectangle area, manually defined by author
    '''
    count = 0.0
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if img[i][j] == 0:
                count += 1
    return float("{0:.2f}".format(round(count / ((row_end - row_start) * (col_end - col_start)), 2)))

def feature_extract(img, isface):
    '''
        define features' start point and end point
    '''
    feature_list = []
    #left_eye
    row_start = 0
    row_end = row_start + 7
    col_start = 0
    col_end = col_start + 7
    left_eye = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(left_eye)

    #forehead
    row_start = 0
    row_end = row_start + 2
    col_start = 6
    col_end = col_start + 5
    forehead = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(forehead)

    #right_eye
    row_start = 0
    row_end = row_start + 7
    col_start = 12
    col_end = col_start + 7
    right_eye = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(right_eye)

    #nose_bridge
    row_start = 2
    row_end = row_start + 9
    col_start = 8
    col_end = col_start + 2
    nose_bridge = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(nose_bridge)

    #left_cheek
    row_start = 7
    row_end = row_start + 6
    col_start = 0
    col_end = col_start + 6
    left_cheek = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(left_cheek)

    #right_cheek
    row_start = 7
    row_end = row_start + 6
    col_start = 12
    col_end = col_start + 7
    right_cheek = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(right_cheek)

    #nose
    row_start = 11
    row_end = row_start + 2
    col_start = 6
    col_end = col_start + 6
    nose = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(nose)

    #mouth
    row_start = 14
    row_end = row_start + 2
    col_start = 4
    col_end = col_start + 10
    mouth = feature_percentage(row_start, row_end, col_start, col_end, img)
    feature_list.append(mouth)
    if isface == 'non-face':
        feature_list.append(0)
    elif isface == 'face':
        feature_list.append(1)
    return feature_list

def write_file(filename, data):
    # title = ['left_eye', 'forehead', 'right_eye', 'nose_bridge', 'left_cheek', 'right_cheek', 'nose', 'mouth']
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        # writer.writerow(title)
        writer.writerows(data)
    f.close()

def main(path, mode):
    namelist = filelist(path)
    isface = path[path.index('/') + 1: -1]
    data = []
    for filename in namelist:
        img = Image.open(path + '/' + filename)
        result_array = threshold.processwithoutmean(img)
        data.append(feature_extract(result_array, isface))
    write_file("result/" + mode + '/' + isface + '_dataset.csv', data)

def filelist(path):
    namelist = []
    names = os.listdir(path)
    for name in names:
        if name[-3:] == 'pgm':
            namelist.append(name)
    return namelist


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

