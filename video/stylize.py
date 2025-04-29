#!/usr/bin/env -S python -m streamlit run

import cv2 as cv
import numpy as np

def stylize(img_bgr, sigma_s=60, sigma_r=0.45):
    stylized = cv.stylization(img_bgr, sigma_s=sigma_s, sigma_r=sigma_r)
    return stylized


if __name__ == '__main__':
    import sys
    img = cv.imread(sys.argv[1])
    stylized = stylize(img)
    cv.imshow('Stylization', stylized)
    cv.waitKey(0)
