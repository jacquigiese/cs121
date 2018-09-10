"""
Author      : Yi-Chieh Wu, <your names here>
Class       : HMC CS 121
Date        : 2018 Sep 05
Description : Homework 1
"""

import numpy as np
import cv2 as cv

######################################################################
# functions
######################################################################

def desteg(img):
    ### ========== TODO : START ========== ###
    # problem a
    # be sure to include a better docstring here!

    pass

    ### ========== TODO : END ========== ###


def steg(img, msg):
    ### ========== TODO : START ========== ###
    # problem b
    # be sure to include a better docstring here!

    pass

    ### ========== TODO : END ========== ###

### ========== TODO : START ========== ###
# problem c (extra credit)

"""
Short Description Here
"""

# steg

# desteg

### ========== TODO : END ========== ###

######################################################################
# main
######################################################################

def main():
    # test desteg (no need to convert)
    fn = "data/steg/small_flag_with_message.png"
    msg = "Wow! This worked!"
    img = cv.imread(fn, cv.IMREAD_COLOR)
    msg2 = desteg(img)
    print("message is \"" + msg2 +  "\"")
    assert(msg == msg2)
    cv.waitKey(0)

    # test desteg (convert color channels)
    fn = "data/steg/small_flag_with_message_bgr.png"
    msg = "Wow! This worked!"
    img = cv.imread(fn, cv.IMREAD_COLOR)
    img = cv.imread(fn, cv.COLOR_RGB2BGR) # swap blue and red
    msg2 = desteg(img)
    print("message is \"" + msg2 + "\"")
    assert(msg == msg2)

    # test steg
    fn = "data/steg/small_flag.png"
    msg = "Pixels are awesome!"
    img = cv.imread(fn, cv.IMREAD_COLOR)
    img2 = steg(img, msg)
    cv.imwrite(fn.split(".")[0] + "_out.png", img2)  # write to file
    msg2 = desteg(img2)
    print("message is \"" + msg2 + "\"")
    assert(msg == msg2)

    ### ========== TODO : START ========== ###
    # problem c (extra credit)

    ### ========== TODO : END ========== ###

if __name__ == "__main__":
    main()