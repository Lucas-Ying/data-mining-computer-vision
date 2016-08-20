from PIL import Image
import numpy
import math
import os


def save_image(img_array, path, subtitle):
    result_image = Image.fromarray(numpy.uint8(img_array))
    result_image.save(path + '/result-' + subtitle + '.png')
    print('Image saved to: ' + path + '/result.png')


# ----------------Edge Detection-----------------

def edge_detection_sobel(img):
    sobel_y = numpy.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
    sobel_x = numpy.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
    return sobel_convolution(img, sobel_x, sobel_y)


# ----------------Noise Cancellation-------------

def noise_cancel_mean(img):
    mean = numpy.array([[1 / 9, 1 / 9, 1 / 9],
                        [1 / 9, 1 / 9, 1 / 9],
                        [1 / 9, 1 / 9, 1 / 9]])
    return onefilter_convolution(img, mean)


def noise_cancel_median(img, filter_pixel):
    return median_convolution(img, filter_pixel)


# ----------------Image Enhancement--------------

def enhancement(img):
    laplacian = numpy.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])
    return onefilter_convolution(img, laplacian)


# ----------------Convolutions-------------------


def sobel_convolution(img, sobel_x, sobel_y):
    img_array = numpy.array(img)
    result_array = numpy.zeros(img_array.shape)
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            img_matrix = img_array[y - 1:y + 2, x - 1:x + 2]
            sx = numpy.sum(sobel_x * img_matrix)
            sy = numpy.sum(sobel_y * img_matrix)
            pixel_val = math.sqrt(math.pow(sx, 2) + math.pow(sy, 2))
            if pixel_val > 255:
                pixel_val = 255
            elif pixel_val < 0:
                pixel_val = 0
            result_array[y, x] = pixel_val
    return result_array


def onefilter_convolution(img, mask):
    img_array = numpy.array(img)
    result_array = numpy.zeros(img_array.shape)
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            img_matrix = img_array[y - 1:y + 2, x - 1:x + 2]
            s = mask * img_matrix
            pixel_val = numpy.sum(s)
            if pixel_val > 255:
                pixel_val = 255
            elif pixel_val < 0:
                pixel_val = 0
            result_array[y, x] = pixel_val
    return result_array


def median_convolution(img, filter_pixel):
    img_array = numpy.array(img)
    result_array = numpy.zeros(img_array.shape)
    n = int((filter_pixel - 1) / 2)
    for x in range(n, img.width - n):
        for y in range(n, img.height - n):
            img_matrix = img_array[y - n:y + (n + 1), x - n:x + (n + 1)]
            pixel_val = numpy.median(img_matrix)
            if pixel_val > 255:
                pixel_val = 255
            elif pixel_val < 0:
                pixel_val = 0
            result_array[y, x] = pixel_val
    return result_array


# ----------------  Main  -------------------

def main():
    while True:
        dir = os.path.dirname(__file__)
        filename = ''
        filter_pixel = 3
        mode = input('Select the following functions by its index:\n'
                     '1. Edge detection\n'
                     '2. Noise cancellation\n'
                     '3. Image enhancement\n'
                     '4. Quit\n')
        if mode == '1':
            filename = dir + '/../project1-images/1.1/test-pattern.tif'
        elif mode == '2':
            filename = dir + '/../project1-images/1.2/ckt-board-saltpep.tif'
            mode += '.'
            mode += input('Select the filter you want to apply:\n'
                          '1. Mean filter\n'
                          '2. Median filter (size 3)\n'
                          '3. Median filter (self-defined size)\n')
            if mode == '2.3':
                mode = '2.2'
                filter_pixel = input('Input the size of your Median filter (e.g. \'5\' for 5*5 median filter):')
        elif mode == '3':
            filename = dir + '/../project1-images/1.3/blurry-moon.tif'
        elif mode == '4':
            break
        print('Loading...')

        if len(filename) == 0:
            print('no file selected')
            break
        path = os.path.dirname(os.path.abspath(filename))
        img = Image.open(filename)
        result_array = None
        if mode == '1':
            result_array = edge_detection_sobel(img)
            save_image(result_array, path, 'sobel')
        elif mode == '2.1':
            result_array = noise_cancel_mean(img)
            save_image(result_array, path, 'mean')
        elif mode == '2.2':
            result_array = noise_cancel_median(img, int(filter_pixel))
            save_image(result_array, path, 'median-'+filter_pixel)
        elif mode == '3':
            result_array = enhancement(img)
            save_image(result_array, path, 'enhancement')
        else:
            print('Invalid function input.')
            break
        if result_array is None:
            print('No output generated.')
            break
        print('')


if __name__ == '__main__':
    main()
