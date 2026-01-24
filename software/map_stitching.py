import cv2
from matplotlib import pyplot as plt
import os

# initialize stitcher
stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)

# load & process images=

#imgL = cv2.imread("C:/Users/benmi/OneDrive - Olin College of Engineering/Pictures/aero-flight-photos/p_1665.jpg")
#imgR = cv2.imread("C:/Users/benmi/OneDrive - Olin College of Engineering/Pictures/aero-flight-photos/p_1666.jpg")

imgs = []
dir = 'C:/Users/benmi/OneDrive - Olin College of Engineering/Pictures/aero-flight-photos/'
for name in os.listdir(dir):
    imgs.append(cv2.imread(os.path.join(dir, name)))


#fig, ax = plt.subplots(1, 2, figsize=(14, 10))
#ax[0].imshow(imgL)
#ax[0].set_title("left")
#ax[0].axis("off")
#ax[1].imshow(imgR)
#ax[1].set_title("right")
#ax[1].axis("off")

def stitch_imgs(images):
    # stitch images
    status, stitched_image = stitcher.stitch(images) #58:63
    print('status:')
    match status:
        case cv2.Stitcher_OK:
            print('OK')
        case cv2.Stitcher_ERR_NEED_MORE_IMGS:
            print('NEED MORE IMGS')
        case cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
            print('HOMOGRAPHY EST FAIL')
        case cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
            print('CAM PARAMS ADJUST FAIL')
        case _:
            print("idk bro")

    if status == cv2.Stitcher_OK:
        stitched_image = cv2.resize(stitched_image,None,fx=1, fy=10, interpolation = cv2.INTER_CUBIC)
        #plt.figure(figsize = (14, 10))
        cv2.imwrite('C:/Users/benmi/OneDrive - Olin College of Engineering/Pictures/aero-flight-photos/wip_stitches/'+str(i)+'.jpg', stitched_image)


for i in range(36):
    stitch_imgs(imgs[58+(i*5):68+(i*5)])
    #print(58+(i*3))
    #print(63+(i*3))

# display stitched images
# if status == cv2.Stitcher_OK:
#     stitched_image = cv2.resize(stitched_image,None,fx=1, fy=10, interpolation = cv2.INTER_CUBIC)
#     plt.figure(figsize = (14, 10))
#     plt.imshow(stitched_image)
#     plt.title('Stitched image')
#     plt.show()