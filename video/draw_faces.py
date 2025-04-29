#!/usr/bin/env python

from pathlib import PurePath
import cv2 as cv

PARENT = PurePath(__file__).parent
SMILY = PARENT / 'data/smily-240.png'
RECT_COLOR = (255, 0, 0)   # B-G-R!
RECT_LINE = 3

def draw_rectangles(img, rectangles):
    ret_img = img.copy()
    for rect in rectangles:
        x0, y0, x1, y1 = rect
        cv.rectangle(ret_img, (x0, y0), (x1, y1), RECT_COLOR, RECT_LINE)

    return ret_img


def draw_smilys(img, rectangles):
    ret_img = img.copy()
    smily = cv.imread(str(SMILY))
    for rect in rectangles:
        x0, y0, x1, y1 = rect
        smily_resized = cv.resize(smily, (x1-x0, y1-y0))
        ret_img[y0:y1, x0:x1] = smily_resized

    return ret_img
