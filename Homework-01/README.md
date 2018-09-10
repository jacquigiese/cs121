# Setup

Let us start by setting up your programming environment for this course.

We will use Python 3.6 for this class. For this week's assignment, you will also need [numpy](http://www.numpy.org/) and [OpenCV](https://opencv.org/).

We *highly recommend* that you use Anaconda package manager, as it makes installing OpenCV much easier. We ran into issues when installing the latest version of OpenCV with package managers such as Pip and Homebrew.

## Install Anaconda

Download the latest version of [Anaconda](https://conda.io/docs/user-guide/install/index.html). Make sure you use the Python 3.6 installer.

## Setup a Python3.6 Environment

If you already have Anaconda installed, make sure you are using Python 3.6.x.

Open up an **Anaconda command prompt**, and run
```
python --version
```

If you do not have the right version, you will have to manage separate Python versions. Anaconda does this through [environments](https://conda.io/docs/user-guide/tasks/manage-python.html).

Create a new environment:
```
conda create -n py36 python=3.6 anaconda
```

Then activate this environment:
```
Windows: activate py36
Mac or Linux: source activate py36
```

To deactivate this environment:
```
Windows: deactivate
Mac or Linux: source deactivate
```

## Install OpenCV

Open up an **Anaconda command prompt**, and run the following command to install OpenCV:
```
conda install opencv
```
[//]: # (conda install -c conda-forge dlib)

We have tested the code with OpenCV 3.4.1, but you can likely use (slightly) older or newer versions without problems. 

[//]: # (DLib 19.9.0)





# Introduction

Fork this repository, and clone it to your machine. Unzip `faces.zip` and `steg.zip`. Your `HW1` directory should look as follows:

```bash
HW1
├── code
|   ├── faces.py                             # code
|   ├── haarcascade_frontalface_default.xml  # haar cascade file
|   └── steg.py                              # code
├── data
|   ├── faces.zip                            # zipped folder
|   ├── faces/raw                            # folder of faces
|   |   └── <files here>
|   ├── steg.zip                             # zipped folder
|   └── steg                                 # folder for steganography
|       └── <files here>
└── README.md
```

You are allowed (and encouraged) to use any of your normal tools (e.g. File Explorer). But you should implement all functionality below in Python.  That is, from the top-level `HW1` directory, we should be able to run `python code/<file>.py` and replicate all your work.

We want to encourage you to explore existing documentation, so we are intentionally not providing you with too much help here. If you find yourself getting stuck, please ask staff via Piazza and office and grutor hours!



# Problem 0: Resume [5 pts]

Let's make sure our resumes are up-to-date. (Bonus: Freshly updated resumes for the upcoming career fair!)

There are several effective styles for resumes. The Career Services Office has some useful [resources](https://www.hmc.edu/career-services/wp-content/uploads/sites/9/2017/08/OSC-Career-Guide-AUG17.pdf) (pages 4-16). Of course, Google (or your preferred search engine) can also provide endless suggestions and examples.

Note that we will peer review these resumes before the actual due date of this assignment, so please have a draft by the peer review date.

Create a top-level `resumes` directory, and add the (post-peer-reviewed) resumes of your team as `resume_<LastnameFirstname>.pdf` (e.g. `resume_WuYiChieh.pdf`).



# Problem 1: Faces [10 pts]

We have downloaded the faces of all CS 121 students from Portal and compressed it into the zip archive `faces.zip`. Your goal is to compute the "average" face across all CS 121 students.

Run the starter code `faces.py`. You should see a "naive" average face. Look through the starter code, and make sure you understand how this naive average is computed.

Your goal is to implement a "smarter" algorithm for averaging faces.

## a. Image Resizing

Your first task is to resize images to the same size.

Implement the missing portion of `crop_images(imgs, resize)`, which should
1) compute the average height and width across all images, and
2) resize images to the average width while maintaining the aspect ratio.

Then uncomment the relevant portion of `main()` to display (and save) the new averaged face.

## b. Face Detection

Your second task is extract faces using OpenCV face detection with Haar Cascades.

Implement `crop_faces(path, path2)`.

- Examples of how Haar Cascades can be used to detect faces can be found online. Feel free to modify any of the examples you find online, though make sure to include links to any resources you used in a comment.

- You should store one face for each provided image. These cropped faces should be stored in a new folder `data/faces/cropped`. If you detect multiple faces, use the rectangle with the largest area.

Then uncomment the relevant portion of `main()` to display (and save) the new averaged face.

## c. Comparison

Include a short (few sentences) block comment comparing the average faces that you found.



# Problem 2: Steganography [20+5 pts]

[Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of embedding hidden messages or codes within another message or, in our case, another image.  Your goal is to both extract a hidden image and embed a hidden image.

[//]: # (This problem asks you to write two functions: a string-hiding function that "deals out" the bits of the string's characters to each pixel in the image, and a string-extracting function that takes an image and returns the string, if any, it hides.)

[//]: # (![Stegosaurus](https://clip2art.com/images/dinosaur-clipart-7.png)
<img src="https://clip2art.com/images/dinosaur-clipart-7.png" width=200px><br/>
<sup><sub>Thanks to CS 35 for this problem!</sub></sup>

## a. Desteganography

Implement `msg = desteg(img)` that (1) takes in a BGR image `img`, (2) extracts the message `msg` that has been steganographically embedded in its lowest-order bits, and (3) returns the message.

*Details*  
- Go through each pixel, one-by-one, and extract the lowest-order bit from its channels. We will only use color images, processed in RGB order (first the red channel, then the green channel, then the blue channel).
- When extracted and placed into a single string (or list), all of the bits should be be in eight-bit blocks, each block corresponding to one character of the message. The final block, indicating the end of message (EOM), is eight `0` bits in a row. Since this is not a printable ASCII character, there's no source of confusion here.

*Example*  
Suppose the encoded message is simply `*`, which corresponds to the 8-bit representation `00101010` (followed by the EOM marker `00000000`). You would start by finding these bits in the image:
1) The red channel of `img[0,0]`     would end in the bit `0` (the initial bit)
2) The green channel of `img[0,0]`   would end in the bit `0` (the next bit)
3) The blue channel of `img[0,0]`    would end in the bit `1` (the next bit)
4) The red channel of `img[0,1]`     would end in the bit `0` (the next bit)
5) The green channel of `img[0,1]`   would end in the bit `1` (the next bit)
6) The blue channel of `image [0,1]` would end in the bit `0` (the next bit)
7) The red channel of `img[0,2]`     would end in the bit `1` (the next bit)
8) The green channel of `img[0,2]`   would end in the bit `0` (the next bit)
9) The blue channel of `img[0,2]`    would end in the bit `0` (the first of 8 0's for EOM)
10) ... and then it would continue in this way for seven more `0` bits, since the message needs to end in 8 `0` bits.

Once retrieved, the 8-bit message would then be converted to the corresponding ASCII character.

*Test Cases*  
We have provide two test cases in `main()`.

*Hints*
- Python has several built-in functions that you may find useful. Look up `bin` and `int` for converting between integer and binary. (Try out these functions from terminal first. Remember to use the correct base for `int`.) Similary, look up `chr` and `ord` for converting between integer and character. (You may not need all of these functions for `desteg`; some may be used for `steg` instead.)
- *Optional*: If you want to make your code more elegant (less copy-paste code), `numpy` can help. In particular, an image is a `np.ndarray`, so check out `np.ndarray.flatten` and `np.ndarray.reshape`. (Again, some of these functions may be used for `steg` instead.)

## b. Steganography

Implement `img2 = steg(img, msg)` that (1) takes in an image BGR `img` and a message `msg`, (2) embeds the message in the lowest-order bits of the image to form a new BGR image `img2`, and (3) returns the new image. (This is the opposite of the function of Part a.)

*Details*  
- We assume the message consists of printable ASCII characters. Each character in message should be converted to an 8-bit binary representation. The 8-bit representation of the message should end with the EOM marker `00000000`.
- The message bits should be encoded in the image in RGB order, one bit per color. Thus, there will be 3 bits changed (or possibly changed) per pixel, each in the least-significant location (last bit).
- If the message is too long to encode in the image, the function should encode what it can (and not end the message with the EOM marker).

*Test Cases*  
We have provide one test case in `main()`.

*Hints*
- Again, you may find Python's built-in functions and `numpy` useful. When converting to binary, be sure to strip the initial `0b` and add initial `0`'s to ensure 8 bits.

*Fun Fact*  
You may have noticed that we wrote out the output image to a file with `_out` appended to the end of the filename. In addition, message-encoded images as saved in PNG format. The reason is that `.png` files are lossless, so your message will be preserved. On the other hand, `.jpg` files are lossy, so your message will be clobbered!

## c. Extra Credit

Instead of embedding and extracting a string message, try embedding an extracting one image (or at least a portion) onto another image! The Wikipedia page has a nice example partway down.)

Specifically, implement
```python
img2 = steg_image(img, img_msg)
img_msg = desteg_image(img)
```
which should hide `img_msg` in `img` and extract it, respectively.

There are many details here, which are up to you to decide how to handle:
- where the `img_msg` "goes"
- how much of the `img_msg` gets represented (you could make it a b/w or a three-bit grayscale image or even use color...)
- whether, beforehand, you scale `img_msg` or not

If you try this part, please include a short block comment with details about your encoding/decoding choices. Also add a exemplar to `main()` (similar to the test case for `steg` above), and add the input images ("base" image and "message" image) and output image (decoded "message" image) to your `HW1` directory.





# Submission

Please ensure that your `HW1` directory has the following file structure:
```bash
HW1
├── code
|   ├── faces.py                             # with your modifications
|   ├── haarcascade_frontalface_default.xml
|   └── steg.py                              # with your modifications
├── data
|   ├── faces.zip
|   ├── faces
|   |   ├── averages                         # folder of averaged faces
|   |   |   └── <files here>
|   |   ├── cropped                          # folder of cropped faces
|   |   |   └── <files here>
|   |   └── raw
|   |       └── <files here>
|   ├── steg.zip
|   └── steg
|       └── <files here>                     # include extra credit
├── README.md
└── resumes
    ├── resume_<username1>.pdf               # your resume
    └── resume_<username2>.pdf               # your resume
```

Remember to update your fork with ALL changes you have made. In general, it is a bad idea<sup>TM</sup> to include output files (or any file that can be regenerated) in a GitHub repo, but we ask you to do so here for the purposes of grading.

Because you have forked our repo, staff will have access to your fork on GitHub. Please do not submit a pull request; otherwise, other students will also have access to your repo. The state of your fork when the homework deadline hits will be considered your submission.
