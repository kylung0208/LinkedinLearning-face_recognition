import PIL.Image
import PIL.ImageDraw
import face_recognition
from face_recognition.api import face_landmarks
import os.path as osp

curdir = osp.dirname(osp.abspath(__file__))

# Load the jpg file into a numpy array 
img_path = osp.join(curdir, "../Ch03/people2.jpg")
print(f"img_path = {img_path}")
image = face_recognition.load_image_file(img_path)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print(f"I found {number_of_faces} face(s) in this phtograph")

# Load the image into a Python Image Library s.t. we can draw on top of it
pil_image = PIL.Image.fromarray(image)

# Create a PIL drawing object to be able to draw lines later
draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for face_landmarks in face_landmarks_list:

    # Loop over each facial feature (eye, nose, mouth, lips, etc)
    for name, list_of_points in face_landmarks.items():

        # Print the location of each facial feature in this image
        print(f"The {name} in this face has the following points: {list_of_points}")

        # Let's trace out each facial feature in the image with a line!
        draw.line(list_of_points, fill='red', width=2)

pil_image.show()