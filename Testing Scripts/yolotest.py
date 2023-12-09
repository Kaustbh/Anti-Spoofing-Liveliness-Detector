from ultralytics import YOLO
import cv2
import cvzone
import math
import time

# cap = cv2.VideoCapture(1)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)
cap = cv2.VideoCapture(0)  # For Video
img2 = cv2.imread('img2.jpeg')
model = YOLO("best2.pt")

# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"
#               ]

# prev_frame_time = 0
# new_frame_time = 0

# while True:
#     new_frame_time = time.time()
#     success, img = cap.read()
#     results = model(img, stream=True)
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding Box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
#             w, h = x2 - x1, y2 - y1
#             cvzone.cornerRect(img, (x1, y1, w, h))
#             # Confidence
#             conf = math.ceil((box.conf[0] * 100)) / 100
#             # Class Name
#             cls = int(box.cls[0])

#             cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

#     fps = 1 / (new_frame_time - prev_frame_time)
#     prev_frame_time = new_frame_time
#     print(fps)

#     cv2.imshow("video",img)
#     if cv2.waitKey(25) & 0xFF ==ord('q'):
#         break


# # import torch
# # print(torch.cuda.is_available())
confidence = 0.8
classNames = ["fake","real"]
results = model(img2, stream=False)
for r in results:
    boxes = r.boxes
    for box in boxes:
        # Bounding Box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img2, (x1, y1, w, h))
        # Confidence
        conf = math.ceil((box.conf[0] * 100)) / 100
        print("confidence:",conf)
        print("\n")
        # Class Name
        cls = int(box.cls[0])

        if conf > confidence:

            if classNames[cls] == 'real':
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            cvzone.cornerRect(img2, (x1, y1, w, h),colorC=color,colorR=color)
            cvzone.putTextRect(img2, f'{classNames[cls].upper()} {int(conf*100)}%',
                                (max(0, x1), max(35, y1)), scale=2, thickness=4,colorR=color,
                                colorB=color)

# fps = 1 / (new_frame_time - prev_frame_time)
# prev_frame_time = new_frame_time
# print("FPS -: ",fps)

cv2.imshow("video",img2)
cv2.waitKey(0)
# if cv2.waitKey(25) & 0xFF ==ord('q'):
#     break
