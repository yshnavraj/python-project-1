# facerec.py
import cv2, numpy, os
from imageDownload import *
size = 2
haar_cascade = cv2.CascadeClassifier('face_cascade.xml')

# Part 1: Create fisherRecognizer
def train_model():
    model = cv2.face.LBPHFaceRecognizer_create() 
    # fn_dir = "face_samples"
    fn_dir = "trainedimages"
    imageDownload()
    print('Training...')
    (images, lables, names, id) = ([], [], {}, 0)

    for (subdirs, dirs, files) in os.walk(fn_dir):
        # Loop through each folder named after the subject in the photos
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            # Loop through each photo in the folder
            for filename in os.listdir(subjectpath):
                # Skip non-image formates
                f_name, f_extension = os.path.splitext(filename)
                if(f_extension.lower() not in ['.png','.jpg','.jpeg','.gif','.pgm']):
                    print("Skipping "+filename+", wrong file type")
                    continue
                path = subjectpath + '/' + filename
                lable = id

                # Add to training data
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1

    # Create a Numpy array from the two lists above
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    # OpenCV trains a model from the images
    # owd = os.getcwd()
    model.train(images, lables)
    # for f in os.listdir(owd):
    #     os.remove(os.path.join(owd, f))
    return (model, names)


# Part 2: Use fisherRecognizer on camera stream
def detect_faces(gray_frame):
    global size, haar_cascade

    # Resize to speed up detection (optinal, change size above)
    mini_frame = cv2.resize(gray_frame, (int(gray_frame.shape[1] / size), int(gray_frame.shape[0] / size)))

    # Detect faces and loop through each one
    faces = haar_cascade.detectMultiScale(mini_frame)
    return faces


def recognize_face(model, frame, gray_frame, face_coords, names):
    (img_width, img_height) = (112, 92)
    recognized = []
    recog_names = []

    for i in range(len(face_coords)):
        face_i = face_coords[i]

        # Coordinates of face after scaling back by `size`
        (x, y, w, h) = [v * size for v in face_i]
        face = gray_frame[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (img_width, img_height))

        # Try to recognize the face
        (prediction, confidence) = model.predict(face_resize)

        # print(prediction, confidence)
        if (confidence<95 and names[prediction] not in recog_names):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            recog_names.append(names[prediction])
            recognized.append((names[prediction].capitalize(), confidence))
        elif (confidence >= 95):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return (frame, recognized)




# # facerec.py
# import cv2, numpy, os
# from sub_facerec import *
# size = 2
# haar_cascade = cv2.CascadeClassifier('face_cascade.xml')

# # Part 1: Create fisherRecognizer
# def train_model():
#     model = cv2.face.LBPHFaceRecognizer_create() 
#     # fn_dir = "./imgTemp.png"

#     print('Training...')

#     (images, lables, names, id) = ([], [], {}, 0)
    
#     # for (subdirs, dirs, files) in os.walk(fn_dir):
#     countTables = getLength()
#     tableList = getTableList()
#     for i in range(countTables):
#         # Loop through each folder named after the subject in the photos
#         # for subdir in dirs:
#         #     names[id] = subdir
#         #     print(names[id])
#         #     subjectpath = os.path.join(fn_dir, subdir)
#             # Loop through each photo in the folder
#         imageList = getImages(tableList[i][0])
#         print(imageList)
#         names[id] = tableList[i][0]
#         imageFile = "imgTemp.png"
#         x = 0
#         for j in range(len(imageList)):
#             imageFile = "imgTemp.png"
#             # print(imageList, len(imageList))
#             with open(imageFile, "wb") as File:
#                File.write(imageList[j][0])
#                File.close()
#             print(x)
#             x += 1
#         filename = imageFile
#         # for filename in os.listdir(subjectpath):
#         # Skip non-image formates
#         f_name, f_extension = os.path.splitext(filename)
#         if(f_extension.lower() not in ['.png','.jpg','.jpeg','.gif','.pgm']):
#             print("Skipping "+filename+", wrong file type")
#             continue
#         path = './' + filename
#         lable = id

#         # Add to training data
#         images.append(cv2.imread(path, 0))
#         lables.append(int(lable))

#         id += 1

#     # Create a Numpy array from the two lists above
#     (images, lables) = [numpy.array(lis) for lis in [images, lables]]
#     # OpenCV trains a model from the images
#     model.train(images, lables)
#     print(len(images))
#     return (model, names)


# # Part 2: Use fisherRecognizer on camera stream
# def detect_faces(gray_frame):
#     global size, haar_cascade

#     # Resize to speed up detection (optinal, change size above)
#     mini_frame = cv2.resize(gray_frame, (int(gray_frame.shape[1] / size), int(gray_frame.shape[0] / size)))

#     # Detect faces and loop through each one
#     faces = haar_cascade.detectMultiScale(mini_frame)
#     return faces


# def recognize_face(model, frame, gray_frame, face_coords, names):
#     (img_width, img_height) = (112, 92)
#     recognized = []
#     recog_names = []
#     print(names)
#     for i in range(len(face_coords)):
#         face_i = face_coords[i]

#         # Coordinates of face after scaling back by `size`
#         (x, y, w, h) = [v * size for v in face_i]
#         face = gray_frame[y:y + h, x:x + w]
#         face_resize = cv2.resize(face, (img_width, img_height))

#         # Try to recognize the face
#         (prediction, confidence) = model.predict(face_resize)

#         # print(prediction, confidence)
#         if (confidence<95 and names[prediction] not in recog_names):
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
#             recog_names.append(names[prediction])
#             recognized.append((names[prediction].capitalize(), confidence))
#         elif (confidence >= 95):
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     print(recognized, recog_names)
#     return (frame, recognized)

