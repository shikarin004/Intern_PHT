# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, default="13.jpg",
# 	help="/home/chanakya/Documents/Intern/Imd/13.jpg")
# args = vars(ap.parse_args())
# # load the original image and show it

image = cv2.imread("/home/chanakya/Documents/Intern/Imd/200.png")
cv2.imshow("RGB", image)
# loop over each of the individual channels and display them
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
	cv2.imshow(name, chan)
# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
# convert the image to the HSV color space and show it
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
# loop over each of the individual channels and display them
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
	cv2.imshow(name, chan)
# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
# convert the image to the L*a*b* color space and show it
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
# loop over each of the individual channels and display them
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
	cv2.imshow(name, chan)
# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
