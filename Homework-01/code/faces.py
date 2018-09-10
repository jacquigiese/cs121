"""
Author      : Yi-Chieh Wu, <your names here>
Class       : HMC CS 121
Date        : 2018 Sep 04
Description : Homework 1
"""

# Only add code inside TODO blocks.

import os
import numpy as np
import cv2 as cv

INF = float("inf")

######################################################################
# functions
######################################################################

def get_files(path):
    """Get full pathname of all files in path directory.

    Parameters
    --------------------
        path   -- directory path, str

    Return
    --------------------
        fns    -- list of filenames, each of type str
    """

    fns = []
    for fn in os.listdir(path):
        full_fn = os.path.join(path, fn)
        if os.path.isdir(full_fn):
            continue
        fns.append(full_fn)
    return fns


def crop_images(imgs, resize=False):
    """Crop images.

    Parameters
    --------------------
        imgs   -- list of images, each of type np.ndarray
        resize -- flag to resize images, bool
    """

    # resize images
    if resize:
        ### ========== TODO : START ========== ###
        # problem a

        # determine average image size
        pass

        # resize to average width while maintaining aspect ratio
        pass
        ### ========== TODO : END ========== ###

    # get minimum image size
    height, width = INF, INF
    for img in imgs:
        img_height, img_width = img.shape[:2]
        if img_height < height:
            height = img_height
        if img_width < width:
            width = img_width

    # crop
    for i, img in enumerate(imgs):
        img_height, img_width = img.shape[:2]
        x = img_width//2 - width//2
        y = img_height//2 - height//2
        roi = img[y:y+height, x:x+width, :]
        #cv.imshow('original', img)
        #cv.imshow('cropped', roi)
        #cv.waitKey(0)
        imgs[i] = roi


def average_image(path, resize=False):
    """Compute average of several images.

    Parameters
    --------------------
        path -- directory path, str
    """

    # read images
    imgs = []
    for fn in get_files(path):
        img = cv.imread(fn)
        imgs.append(img)

    # crop images
    crop_images(imgs, resize=resize)

    # average
    height, width = imgs[0].shape[:2]
    avg_img = np.zeros((height,width,3), np.float32())
    for img in imgs:
        avg_img += img
    avg_img = avg_img / len(imgs)
    avg_img = np.rint(avg_img).astype(np.uint8)  # convert to uint8

    return avg_img


def crop_faces(path, path2):
    """Crop faces using face detection.

    Parameters
    --------------------
        path  -- directory path of input faces, str
        path2 -- directory path of output faces, str
    """

    ### ========== TODO : START ========== ###
    # problem b

    # make directory
    pass

    # process images
    pass
    ### ========== TODO : END ========== ###


######################################################################
# main
######################################################################

def main():
    averages_dir = os.path.join("data/faces/averages")
    if not os.path.exists(averages_dir):
        os.mkdir(averages_dir)

    img = average_image("data/faces/raw")
    cv.imshow("naive average", img)
    cv.imwrite(os.path.join(averages_dir, "avg_naive.jpg"), img)
    cv.waitKey(0)

    ### ========== TODO : START ========== ###
    ### Uncomment these lines after implementing code

    # problem a
    """
    img = average_image("data/faces/raw", resize=True)
    cv.imshow("naive resized average", img)
    cv.imwrite(os.path.join(averages_dir, "avg_resized.jpg"), img)
    cv.waitKey(0)
    """

    # problem b
    """
    crop_faces("data/faces/raw", "data/faces/cropped")
    img = average_image("data/faces/cropped", resize=True)
    cv.imshow("face detection average", img)
    cv.imwrite(os.path.join(averages_dir, "avg_detect.jpg"), img)
    cv.waitKey(0)
    """

    # problem c
    """
    Short Description Here
    """
    ### ========== TODO : END ========== ###

if __name__ == "__main__":
    main()
