__author__ = 'bernardo'

import cv2
import cPickle
import random
import numpy as np

imgsize = 50


def save_obj(obj, name):
    with open( str(name) + '.txt', 'wb') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open( str(name) + '.txt', 'rb') as f:
        return cPickle.load(f)


class numbers:
    number = 0
    sinapsis = None
    value = 0
    threshold = 1


def main():
    numberL = []
    #cv2.namedWindow('image0', cv2.WINDOW_NORMAL)
    """ cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image3', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image4', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image5', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image6', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image7', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image8', cv2.WINDOW_NORMAL)"""

    for x in xrange(0,9):
        nnum = numbers()
        nnum.sinapsis = []
        nnum.value = 0
        nnum.number = x
        nnum.sinapsis = np.zeros((50, 50, 1), np.float128)
        for y1 in xrange(0,50):

            huu = []
            for y2 in xrange(0,50):
                nnum.sinapsis[y1,y2] = round(random.uniform(0.1, 1),2)

        print len(nnum.sinapsis)
        numberL.append(nnum)
        del nnum


    nump = 1

    teachfor = 100


    gray_img1 = (255-cv2.cvtColor(cv2.imread('numbers/1_a.png'), cv2.COLOR_BGR2GRAY))
    gray_img2 = (255-cv2.cvtColor(cv2.imread('numbers/2_a.png'), cv2.COLOR_BGR2GRAY))
    gray_img3 = (255-cv2.cvtColor(cv2.imread('numbers/3_a.png'), cv2.COLOR_BGR2GRAY))



    while True:
        nump += 1
        real_num = (nump % 3) + 1
        print "number--------------: " + str(real_num)
        read_img = str(real_num)+ "_a"
        if real_num == 1:
            gray_img = gray_img1
        elif real_num == 2:
            gray_img = gray_img2
        elif real_num == 3:
            gray_img = gray_img3

        for x in xrange(0,9):
            for y1 in xrange(0,50):
                for y2 in xrange(0,50):
                    if (gray_img[y1, y2]) > 150:
                        numberL[x].value += (numberL[x].sinapsis[y1,y2])
        #cv2.imshow("image0", numberL[0].sinapsis)
        """
        cv2.imshow("image1", numberL[1].sinapsis)
        cv2.imshow("image2", numberL[2].sinapsis)
        cv2.imshow("image3", numberL[3].sinapsis)
        cv2.imshow("image4", numberL[4].sinapsis)
        cv2.imshow("image5", numberL[5].sinapsis)
        cv2.imshow("image6", numberL[6].sinapsis)
        cv2.imshow("image7", numberL[7].sinapsis)
        cv2.imshow("image8", numberL[8].sinapsis)"""

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        newlist = sorted(numberL, key=lambda x: x.value, reverse=True)

        for x in xrange(0,9):
            print str(newlist[x].number) + "  :" + str(newlist[x].value)

        guess = newlist[0].number

        if nump < teachfor:
            realnum = real_num
        else:
            print "Guessed: " + str(guess)
            realnum = raw_input("it was? ")

        if str(realnum) != str(guess):
            for y1 in xrange(0,50):
                for y2 in xrange(0,50):
                    if (gray_img[y1,y2]) > 150:
                        numberL[int(realnum)].sinapsis[y1,y2] += 0.5
            print "FALSE"
        else:
            print "TRUE"

        for y1 in xrange(0,50):
            for y2 in xrange(0,50):
                if numberL[int(realnum)].sinapsis[y1,y2] > 0.2:
                    numberL[int(realnum)].sinapsis[y1,y2] = (numberL[int(realnum)].sinapsis[y1,y2] - 0.1)



main()
