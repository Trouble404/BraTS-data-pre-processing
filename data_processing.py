import sys
import numpy as np
import scipy
import scipy.interpolate as interpolate
import scipy.ndimage
from skimage import exposure

# data augmentation function

# Translation

def translateit(image, offset, isseg=False):
    order = 0 if isseg == True else 5
    image = scipy.ndimage.interpolation.shift(image, (int(offset[0]), int(offset[1]), 0), order=order, mode='nearest')
    image[image<0]=0
    return image

# Rotation
def rotateit(image, theta, isseg=False):
    order = 0 if isseg == True else 5
    image = scipy.ndimage.rotate(image, float(theta), reshape=False, order=order, mode='nearest')
    image[image<0]=0   
    return image

# Flip
def flipit(image, axes):
    if axes[0]:
        image = np.fliplr(image)
    if axes[1]:
        image = np.flipud(image)
    image[image<0]=0
    return image

# Gamma
def gamma_correction(image, value):
    image = exposure.adjust_gamma(image, value)
    image[image<0]=0
    return image

def data_augmentaion(orignal_image):
    np.random.seed()
    numTrans = np.random.randint(1, 6 ,size=1)
    allowedTrans = [0, 1, 2, 3, 4]
    whichTrans = np.random.choice(allowedTrans, numTrans, replace=False)

    if 0 in whichTrans: # Translation
        i = np.random.randint(-20,20, size=1)[0]
        j = np.random.randint(-20,20, size=1)[0]
        orignal_image = translateit(orignal_image, [i,j])

        return orignal_image

    if 1 in whichTrans: # Rotation
        i = np.random.randint(0,360, size=1)[0]
        orignal_image = rotateit(orignal_image, i)

        return orignal_image

    if 2 in whichTrans: # Flip
        i = np.random.randint(0,3, size=1)[0]
        if i == 0:
            j = [0, 1]
        if i == 1:
            j = [1, 0]
        if i == 2:
            j = [1, 1]
        orignal_image = flipit(orignal_image, j)

        return orignal_image
    
    if 3 in whichTrans: # Gamma
        i = np.random.uniform(0.9, 1.1)
        orignal_image = gamma_correction(orignal_image, i)

        return orignal_image

    if 4 in whichTrans: # Orignal

        return orignal_image
    

