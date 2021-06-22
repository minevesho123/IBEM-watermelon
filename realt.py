from pandas.core.frame import DataFrame
import cv2
import numpy as np
import pandas as pd
import csv
import os
import time
from core.function import *
import core.utils as utils
from datetime import datetime
import random
# Load Yolo
net = cv2.dnn.readNet(
    "weights/custom-yolov4-tiny-detector_last.weights", "cfg/custom-yolov4-tiny-detector.cfg")
classes = []
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


#fileVariable = open('documentation/data.csv', 'r+')
# fileVariable.truncate(0)
# fileVariable.close()

n = random.randint(0, 100)
dir = "documentation/"
no = datetime.now()
dst = no.strftime('%m/_d_%Y_%H_%M')

sp = os.path.join(dir, str(dst) + str(n) + '.csv')
dict = {}
df = pd.DataFrame(dict)
df.to_csv(sp, index=False)


headerList = ['Name', 'Date', 'Time', 'Humidity',
              'Temperature', 'Ethylene Readings', 'Fruit Condition']
with open(sp, 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
    dw.writeheader()


def markdetection(name):
    with open(sp, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%m/%d/%Y, %H:%M"%S')
            f.writelines(f'\n{name},{dtString}')


pathfile = 'C:/Users/agbaj/Documents/possible watermeon api/new/final model for project/documentation/'

# Loading image
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_PLAIN
frame_id = 0
count = 0
while True:
    # start_time = time.time()
    _, frame = cap.read()
    frame_id += 1

    height, width, channels = frame.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(
        frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # print(len(boxes))

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)
    print(indexes)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label + " " + str(round(confidence, 2)),
                        (x, y + 30), font, 3, color, 3)

            roi_color = frame[y:y + h, x:x + w]
            path = 'detection/crop/watermelon'

            start_time = time.time()
            counter = 'watermelon' + str(count) + '.jpg'
            cv2.imwrite(os.path.join(path, counter), roi_color)
            time.sleep(3.0 - time.time() + start_time)
            print(counter)

            markdetection(counter)

            count += 1

    cv2.imshow("Image", frame)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

    # time.sleep(1.0 - time.time() + start_time)

# cap.release()
# cv2.destroyAllWindows()
