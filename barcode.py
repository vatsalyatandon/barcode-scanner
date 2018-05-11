from __future__ import print_function
from pyzbar.pyzbar import pyzbar
import numpy as np
import cv2

def decode(im) :
	decodedObjects = decode(im)

	for obj in decodedObjects:
		print('Type : ', obj.type)
		print('Data : ', obj.data, '\n')
	return decodedObjects

def display(im, decodedObjects) :
	for decodedObject in decodedObjects:
		points = decodedObject.location

		if len(points) > 4 :
			hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
			hull = list(map(tuple, np.squeeze(hull)))
		else :
			hull = points

		n= len(hull)

		for j in range(0,n):
			cv2.line(im, hull[j], hull[(j+1)%n], (255,0,0),3)

	cv2.imshow("Results", im);
	cv2.waitKey(0);

if __name__ == '__main__':

	im = cv2.imread('Barcodescan.jpg')

	decodedObjects = decode(im)
	display(im,decodedObjects)
