# Loads images and passes to pipeline
from pipeline import Pipeline
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__=='__main__':
    # test image is 'calibration2.jpg' right now
    img = cv2.imread('../data\camera_cal\calibration6.jpg')
    pipeline = Pipeline()
    processed_img = pipeline.run_pipeline(img)

    # Draw both images together
    plt.figure(0)
    plt.subplot(1,2,1)
    plt.imshow(img , cmap='gray')
    plt.title('Original')
    plt.subplot(1,2,2)
    plt.imshow(processed_img)
    plt.title('Processed')
    plt.waitforbuttonpress()
