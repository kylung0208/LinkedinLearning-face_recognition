import PIL.Image
import PIL.ImageDraw
import face_recognition
import os.path as osp


curdir = osp.dirname(osp.abspath(__file__))

# Load the jpg file into a numpy array 
img_path = osp.join(curdir, "../Ch03/people.jpg")
print(f"img_path = {img_path}")
image = face_recognition.load_image_file(img_path)

# Generate the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found!")
else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)