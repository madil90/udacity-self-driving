# Loads images and passes to pipeline
from pipeline import Pipeline
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

def toRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

if __name__=='__main__':
    cap = cv2.VideoCapture('../data/project_video.mp4')
    n = 0
    start_time = time.time()
    pipeline = Pipeline()
 
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
        print("Unable to read camera feed")
    
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    # is_gray = True

    print(frame_width, frame_height)
    
    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('../data/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1202,621))
    # out = cv2.VideoWriter('../data/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1202,621), isColor=False)
    

    # frame no used for testing to limit no of frames used
    frame_no = 0
    allowed_min_frame = 0
    allowed_max_frame = 30

    while(True):

        # reading the video 
        ret, img = cap.read()
        
        if ret == True: 
            # test image is 'calibration2.jpg' right now
            plt.ion()
            # img = cv2.imread('../data/test_images/test6.jpg')
            # if img is None:
            #     print('Image not found')
            #     exit()

            # check if frame no is allowed 
            frame_no += 1
            if (frame_no < allowed_min_frame or \
                frame_no > allowed_max_frame):
                continue


            processed_img = pipeline.run_pipeline(img)
            frame_height, frame_width, channels = processed_img.shape

            # Draw both images together
            # plt.figure(0)
            # plt.subplot(1,2,1)
            # plt.imshow(toRGB(img))
            # plt.title('Original')
            # plt.subplot(1,2,2)
            # plt.imshow(toRGB(processed_img))
            # plt.title('Processed')
            # plt.pause(0.05)

            # print(processed_img.shape)
            out.write(cv2.resize(processed_img,(frame_width, frame_height)))

            print('Processed ', frame_no, 'th frame')
        else:
            break
    
    elapsed_time = time.time() - start_time
    print('Total Time taken is ', elapsed_time)

    out.release()
    cap.release()
    cv2.destroyAllWindows()
