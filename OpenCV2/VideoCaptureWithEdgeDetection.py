import cv2
myCam = cv2.VideoCapture(0)

def captureImage():
	global myCam
	ret_Val, img = myCam.read()
	return img

def showImage(ix):
	cv2.imshow('my Camera', ix)
	edges = cv2.Canny(ix, 100,200)
	cv2.imshow('Edges',edges)

while True:
	ixl = captureImage()
	showImage(ixl)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.release()

cv2.destroyAllWindows()
