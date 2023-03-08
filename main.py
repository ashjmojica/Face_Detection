import cv2

# Fill the cascade by using cv2. CascadeClassifier function
f_cascade = cv2.CascadeClassifier('default.xml')

# Scan the image for faces
images_for_faces = cv2.imread('test.jpeg')

# Transform to grayscale
gray_scale = cv2.cvtColor(images_for_faces, cv2.COLOR_BGR2GRAY)

# Find and identify faces
identified_faces = f_cascade.detectMultiScale(gray_scale, 1.1, 4)

# Outline green rectangles on the faces
print("Face Detection Program Identified {0} faces.".format(len(identified_faces)))

# Apply cv2.rectangle() attribute to draw a rectangle with green borders of thickness of 4 px
for (a, b, c, d) in identified_faces:
    cv2.rectangle(images_for_faces, (a, b), (a+c, b+d), (0, 255, 0), 4)

# Show it in a new window until a key is pressed by using waitKey() attribute
cv2.imshow('img', images_for_faces)
# Open it in a new window by using waitKey() attribute
cv2.waitKey()