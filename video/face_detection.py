#!/usr/bin/env python

from pathlib import PurePath
import cv2 as cv

PARENT = PurePath(__file__).parent
PROTO_TEXT = PARENT / 'data/deploy.prototxt'
WEIGHT = PARENT / 'data/res10_300x300_ssd_iter_140000_fp16.caffemodel'
PROB_THRESH = 0.3

def prepare_model():
    net = cv.dnn.readNet(WEIGHT, PROTO_TEXT, 'Caffe')
    return net


def detect(net, img, thresh=PROB_THRESH):
    blob = cv.dnn.blobFromImage(img, size=(300, 300), mean=(104, 177, 123))
    net.setInput(blob)
    pred = net.forward()

    rectangles = []
    for i in range(pred.shape[2]):
        conf = pred[0, 0, i, 2]
        if conf > thresh:
            x0 = int(pred[0, 0, i, 3] * img.shape[1])
            y0 = int(pred[0, 0, i, 4] * img.shape[0])
            x1 = int(pred[0, 0, i, 5] * img.shape[1])
            y1 = int(pred[0, 0, i, 6] * img.shape[0])
            if x1 < x0:
                x0, x1 = [x1, x0]
            if y1 < y0:
                y0, y1 = [y1, y0]
            rectangles.append( (x0, y0, x1, y1) )

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
