from PIL import Image
import numpy
import math
import os


def save_image(img_array, path, subtitle):
    result_image = Image.fromarray(numpy.uint8(img_array))
    result_image.save(path + '/result-' + subtitle + '.png')
    print('Image saved to: ' + path + '/result.png')


# ----------------Noise Cancellation-------------

def smooth_mean(img, width, height):
    mean = numpy.array([[1 / 9, 1 / 9, 1 / 9],
                        [1 / 9, 1 / 9, 1 / 9],
                        [1 / 9, 1 / 9, 1 / 9]])
    return convolution(img, mean, width, height)


# ----------------Convolution-------------------


def convolution(img, mean, width, height):
    img_array = numpy.array(img)
    result_array = numpy.zeros(img_array.shape)
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            img_matrix = img_array[y - 1:y + 2, x - 1:x + 2]
            s = mean * img_matrix
            pixel_val = numpy.sum(s)
            if pixel_val > 255:
                pixel_val = 255
            elif pixel_val < 0:
                pixel_val = 0
            result_array[y, x] = pixel_val
    return result_array


# ----------------Threshold-------------------

def otsu(img_array, width, height):
    threshold = 0
    w0 = w1 = u0tmp = u1tmp = u0 = u1 = u = deltaTmp = deltaMax = 0.0
    pixelCount = [0 for i in range(256)]
    pixelPro = [0.0 for i in range(256)]
    for i in range(0, width):
        for j in range(0, height):
            pixelCount[img_array[j][i].astype(numpy.int64)] += 1
    for i in range(256):
        pixelPro[i] = pixelCount[i] / float(width * height)
    for i in range(256):
        w0 = w1 = u0tmp = u1tmp = u0 = u1 = u = deltaTmp = 0.0
        for j in range(256):
            if j <= i:
                w0 += pixelPro[j]
                u0tmp += j * pixelPro[j]
            else:
                w1 += pixelPro[j]
                u1tmp += j * pixelPro[j]
        if w0 == 0.0:
            continue
        u0 = u0tmp / w0
        if w1 == 0.0:
            continue
        u1 = u1tmp / w1
        u = u0tmp + u1tmp
        deltaTmp = w0 * math.pow((u0 - u), 2) + w1 * math.pow((u1 - u), 2)
        if deltaTmp > deltaMax:
            deltaMax = deltaTmp
            threshold = i
    return threshold


def comparison(img_array, width, height, threshold):
    result_array = numpy.zeros(img_array.shape)
    for x in range(width):
        for y in range(height):
            if img_array[y][x] > threshold:
                result_array[y][x] = 255
            else:
                result_array[y][x] = 0
    return result_array


# ----------  with mean filter  -------------

def processimg(img):
    smooth_array = smooth_mean(img, img.width, img.height)
    threshold = otsu(smooth_array, img.width, img.height)
    result_array = comparison(smooth_array, img.width, img.height, threshold)
    return result_array


# ----------  without mean filter  ----------

def processwithoutmean(img):
    img_array = numpy.array(img)
    threshold = otsu(img_array, img.width, img.height)
    result_array = comparison(img_array, img.width, img.height, threshold)
    return result_array

# ----------------  Main  -------------------

def main():
    dir = os.path.dirname(__file__)
    filename = dir + '/../project1-images/2.1/hubble.tif'
    path = os.path.dirname(os.path.abspath(filename))
    img = Image.open(filename)
    result_array = processimg(img)
    save_image(result_array, path, 'mean-otsu')

if __name__ == '__main__':
    main()
