#!/usr/bin/env python

from pathlib import PurePath
import cv2 as cv
import numpy as np

PARENT = PurePath(__file__).parent
HAAR_FILE = PARENT / 'data/haarcascade_frontalcatface.xml'

def prepare_model():
    cascade = cv.CascadeClassifier(str(HAAR_FILE))
    return cascade


def detect(net, img, thresh=None):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.equalizeHist(gray, gray);
    objects = net.detectMultiScale(gray) 

    rectangles = []
    for rect in objects:
        x0, y0, w, h = rect
        rectangles.append( (x0, y0, x0+w, y0+h) )

    return rectangles



if __name__ == '__main__':
    import sys
    from draw_faces import draw_rectangles, draw_smilys

    img = cv.imread(sys.argv[1])

    net = prepare_model()
    rectangles = detect(net, img)
    print(f'{len(rectangles)} faces.')

    boxes = draw_rectangles(img, rectangles)
    cv.imshow('Face detection', boxes)

    smilys = draw_smilys(img, rectangles)
    cv.imshow('Laughing Man', smilys)
    cv.waitKey(0)
