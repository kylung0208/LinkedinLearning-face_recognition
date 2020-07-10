from os import curdir
import PIL.Image
import PIL.ImageDraw
import face_recognition # to access the face detection model in dlib
import os.path as osp

curdir = osp.dirname(osp.abspath(__file__))
print(f"curdir = {curdir}")

# Load the jpg file into a numpy array 
img_path = osp.join(curdir, "people.jpg")
image = face_recognition.load_image_file(img_path)

# find all the faces in the image (pretrained HOG model)
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print(f"I need {number_of_faces} face(s) in this photograph")

# Load the image into a python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:

    # Print the location of each face in this image, Each face is a list of co-ordinates in (top, right, bottom, left) order.
    top, right, bottom, left = face_location
    print(f"A face is located at pixel location Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")

    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")

# Display the image on screen
pil_image.show()