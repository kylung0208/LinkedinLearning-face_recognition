import os.path as osp
import face_recognition


cur_dir = osp.dirname(osp.abspath(__file__))

# Load the known images
image_of_person_1 = face_recognition.load_image_file(osp.join(cur_dir, "person1.jpeg"))
image_of_person_2 = face_recognition.load_image_file(osp.join(cur_dir, "person2.jpeg"))
image_of_person_3 = face_recognition.load_image_file(osp.join(cur_dir, "person3.jpeg"))

# Get the face encoding of each person. This can fail if no one is found in the photo
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]
person_3_face_encoding = face_recognition.face_encodings(image_of_person_3)[0]

# Create a list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
    person_3_face_encoding
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file(osp.join(cur_dir, "unknown1.jpeg"))
print("unkonwn image loaded...")
# Get face encodings for any people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person i nthe photo, so we need to loop over each face
for unknown_face_encoding in unknown_face_encodings:

    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

    name = "Unknown"
    print(f"results = {results}")

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"
    
    print(f"Found {name} in the photo!")