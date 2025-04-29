#!/usr/bin/env python

import cv2 as cv
import numpy as np
import requests

MAX_WIDTH = 1024

def limit_size(img, max_width=MAX_WIDTH):
    if max_width is None:
        return img

    factor = min([max_width/wh for wh in img.shape])
    if factor < 1:
        img = cv.resize(img, dsize=None, fx=factor, fy=factor)

    return img


def bytes_to_ndarray(buf):
    arr = np.frombuffer(buf, np.uint8)
    img_bgr = cv.imdecode(arr, cv.IMREAD_COLOR)
    return img_bgr


def uploaded_to_ndarray(uploaded, max_width=MAX_WIDTH):
    buf = uploaded.getvalue()
    img = bytes_to_ndarray(buf)
    if img is None:
        raise Exception('Failed to read UploadedFile.')

    return limit_size(img, max_width)


def url_to_ndarray(url, max_width=MAX_WIDTH):
    resp = requests.get(url, headers={'User-agent': 'MyRequest'})
    if resp.status_code != 200:
        raise Exception('Failed to read URL.')

    img = bytes_to_ndarray(resp.content)

    return limit_size(img, max_width)



if __name__ == '__main__':
    import sys
    from io import BytesIO

    max_width = 480
    file = sys.argv[1]
    if file.startswith('http'):
        img = url_to_ndarray(file, max_width)
    else:
        with open(sys.argv[1], 'rb') as fp:
            buf = fp.read()
            uploaded = BytesIO(buf)
            img = uploaded_to_ndarray(uploaded, max_width)

    cv.imshow('Test', img)
    print(img.shape)
    cv.waitKey(0)
