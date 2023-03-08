import cv2

Vcapture = cv2.VideoCapture(0)

# Fill the cascade by using cv2. CascadeClassifier function
f_cascade = cv2.CascadeClassifier('default.xml')

while(True):
	# Capture frame-by-frame
	ret, frm = Vcapture.read()

	# Our operations on the frame come here
	gray_scale = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

	# Find and identify faces
	identified_faces = f_cascade.detectMultiScale(gray_scale, 1.1, 4)

	# Outline green rectangles on the faces
	print("Face Detection Program Identified {0} faces.".format(len(identified_faces)))

	# Apply cv2.rectangle() attribute to draw a rectangle with green borders of thickness of 4 px
	for (a, b, c, d) in identified_faces:
		cv2.rectangle(frm, (a, b), (a + c, b + d), (0, 255, 0), 4)

	# Show it in a new window until 'q' is pressed by using waitKey() attribute
	cv2.imshow('frame', frm)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
Vcapture.release()
cv2.destroyAllWindows()
